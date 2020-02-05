
all: generate

countrytagger/data/allCountries.zip:
	curl -s -o countrytagger/data/allCountries.zip https://download.geonames.org/export/dump/allCountries.zip

geonames: countrytagger/data/allCountries.zip

generate: geonames
	python countrytagger/generate.py