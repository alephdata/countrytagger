
data/allCountries.zip:
	curl -s -o data/allCountries.zip https://download.geonames.org/export/dump/allCountries.zip

geonames: data/allCountries.zip
	unzip -p data/allCountries.zip | grep "\t(ADM1\|ADM2\|PCLI\|PPLC\|PPLA)\t" >services/ingest-file/data/geonames.txt
