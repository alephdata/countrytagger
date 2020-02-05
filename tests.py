import unittest

import countrytagger


class TestCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_get_place(self):
        code, score, country = countrytagger.tag_place('Berlin')
        assert country == 'de'
        code, score, country = countrytagger.tag_place('Prague...')
        assert country == 'cz'
        code, score, country = countrytagger.tag_place('Budapress')
        assert country is None

    def test_tag_text(self):
        x = "This is a text about Quebec province in Canada."
        res = list(countrytagger.tag_text_countries(x))
        assert len(res) == 2
        countries = set([c for _, _, c in res])
        assert 'ca' in countries
        assert len(countries) == 1

        x = "This is a text about Nicosia in Bavaria."
        res = list(countrytagger.tag_text_countries(x))
        assert len(res) == 2
        countries = [c for _, _, c in res]
        assert 'cy' in countries
        assert 'ca' not in countries


unittest.main(verbosity=2)
