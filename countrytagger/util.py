import csv
import pathlib
from normality import normalize


# https://www.geonames.org/export/codes.html
CODES = {
    'PCLI': 1.0,
    'PCL': .9,
    'PCLD': .6,
    'PPLC': .5,  # capital
    'PPLG': .4,  # government
    'ADM1': .3,
    # 'PPLA': 10,  # first-order city
    # 'ADM2': 2,
    # 'ADMD': 1,
}

DATA_PATH = pathlib.Path(__file__).parent.absolute().joinpath('data')
PLACES_PATH = DATA_PATH.joinpath('places.csv')


def text_norm(text):
    return normalize(text, ascii=True)


def iter_places():
    with open(PLACES_PATH, 'r', encoding='utf-8') as fh:
        for row in csv.DictReader(fh):
            yield row
