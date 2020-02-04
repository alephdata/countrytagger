import io
import csv
import zipfile
import dataset
from normality import normalize
from collections import defaultdict

SOURCE_DATA = 'data/allCountries.zip'
# https://www.geonames.org/export/codes.html
CODES = {
    'PCLI': 100,
    'PCL': 70,
    'PCLD': 50,
    'PPLC': 30,  # capital
    'ADM1': 20,
    # 'PPLA': 10,  # first-order city
    'PPLG': 10,  # government
    # 'ADM2': 2,
    # 'ADMD': 1,
}

db = dataset.connect('sqlite:///data/places.sqlite3')
places = db['places']


def text_norm(text):
    text = normalize(text, ascii=True)
    return ' %s ' % text


def read_rows():
    with zipfile.ZipFile(SOURCE_DATA) as zip:
        with zip.open('allCountries.txt') as fh:
            fhtext = io.TextIOWrapper(fh, encoding='utf-8')
            for row in csv.reader(fhtext, delimiter='\t'):
                yield row


# terms = defaultdict(list)
# places = defaultdict(list)
for row in read_rows():
    country = row[8].lower().strip()
    if not len(country):
        continue
    type_ = row[7]
    if type_ not in CODES:
        continue
    # print(row)
    names = set(row[3].split(','))
    names.add(row[1])
    names.add(row[2])
    for name in names:
        if len(name) < 4:
            continue
        norm = text_norm(name)
        # for term in norm.split(' '):
        #     terms[term].append(country)
        places.insert({
            'norm': norm,
            'name': name,
            'type': type_,
            'country': country
        })
        # places[norm].append((name, type_, country))
        # print(name, norm, type_, country)
        # aho.add_word(norm, country)

# for term, countries in terms.items():
#     print(term, len(countries), len(set(countries)))

# for (norm, inst) in places.items():
#     if len(inst) > 1:
#         print(norm, inst)
