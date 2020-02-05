import io
import csv
import zipfile
from collections import defaultdict

from countrytagger.util import text_norm, CODES
from countrytagger.util import DATA_PATH, PLACES_PATH

SOURCE_DATA = DATA_PATH.joinpath('allCountries.zip')


def read_rows():
    with zipfile.ZipFile(SOURCE_DATA) as zip:
        with zip.open('allCountries.txt') as fh:
            fhtext = io.TextIOWrapper(fh, encoding='utf-8')
            for row in csv.reader(fhtext, delimiter='\t'):
                yield row


def generate_places():
    places = defaultdict(list)
    for row in read_rows():
        country = row[8].lower().strip()
        if not len(country):
            continue
        code = row[7]
        if code not in CODES:
            continue
        # print(row)
        names = set(row[3].split(','))
        names.add(row[1])
        names.add(row[2])
        for name in names:
            norm = text_norm(name)
            if norm is None or len(norm) < 4:
                continue
            places[norm].append((name, code, country))

    with open(PLACES_PATH, 'w', encoding='utf-8') as fh:
        writer = csv.writer(fh, dialect=csv.unix_dialect)
        writer.writerow(['name', 'code', 'country'])
        for (norm, inst) in places.items():
            countries = set([c for _, _, c in inst])
            if len(countries) > 1:
                continue
            codes = set([c for _, c, _ in inst])
            code = max(codes, key=lambda c: CODES.get(c))
            for (name, cd, country) in inst:
                if cd == code:
                    writer.writerow([name, code, country])


if __name__ == '__main__':
    generate_places()
