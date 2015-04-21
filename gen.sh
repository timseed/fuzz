#!/bin/bash
echo "Get data - 5K records "
curl "https://www.mockaroo.com/af9cfb00/download?count=5000&key=a32b6110" >> "basic.csv"
echo "Reindex and create people"
cat basic.csv | cut -d ',' -f 2- | nl -n ln  | sed -e 's/[[:space:]]\+/,/g' -e 's/^1,/id,/' > people.csv
