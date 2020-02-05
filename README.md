# countrytagger

This library finds the names of places in a string of text and tries to associate
them with countries. The goal is to tag a piece (or set) of text with country
metadata. The place names are derived from the GeoNames database, and they include
names of countries, major administrative areas and large cities. Place names that
are used in several countries are not used.

## Usage

```python
import countrytagger

# match in a string using sequential matching:
text = 'I am in Berlin'
for (code, score, country) in countrytagger.tag_text_countries(text):
    print(score, country)

# find precise matches:
code, score, country = countrytagger.tag_place('Berlin')
```

## Building the data

You can re-generate the place database like this:

```bash
$ make generate
```

This will download GeoNames and parse it into the format used by this library.