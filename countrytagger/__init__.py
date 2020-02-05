from threading import RLock
from ahocorasick import Automaton
from countrytagger.util import text_norm, iter_places
from countrytagger.util import CODES

__version__ = '0.1.0'

AUTOMATA = {}
compiler_lock = RLock()


def _get_automaton(normalizer):
    with compiler_lock:
        if normalizer in AUTOMATA:
            return AUTOMATA.get(normalizer)
        aho = Automaton()
        for place in iter_places():
            name = place.get('name')
            norm = normalizer(name)
            value = (place.get('code'), place.get('country'))
            aho.add_word(norm, value)
        aho.make_automaton()
        AUTOMATA[normalizer] = aho
        return aho


def tag_text_countries(text, normalizer=text_norm):
    """Return an iterator of tuples with (level, score, country)
    representing each geographic designation in the dataset and
    how likely it is indicative of a given country."""
    norm = normalizer(text)
    if norm is None:
        return
    aho = _get_automaton(normalizer)
    for end, (code, country) in aho.iter(norm):
        yield (code, CODES.get(code, 0.0), country)


def tag_place(place_name, normalizer=text_norm):
    norm = normalizer(place_name)
    if norm is None:
        return
    aho = _get_automaton(normalizer)
    try:
        code, country = aho.get(norm)
        return (code, CODES.get(code, 0.0), country)
    except KeyError:
        return (None, 0.0, None)


if __name__ == '__main__':
    x = "This is a text about Quebec province in Canada."
    for res in tag_text_countries(x):
        print(res)

    x = "This is a text about Nicosia in Bavaria."
    for res in tag_text_countries(x):
        print(res)

    print(tag_place("Prague.."))
    print(tag_place("Budapress"))
