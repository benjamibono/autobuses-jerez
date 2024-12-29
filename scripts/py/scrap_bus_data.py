import json
from lxml import etree
import requests

lines = list(range(1, 19))

bus_data = []

for line in lines:

	print(f"Obteniendo datos linea {line}")

	html = requests.post("https://www.comujesa.es/index.php?id=listar_c", data={'valorLinea': line})

	parser = etree.HTMLParser()
	tree = etree.fromstring(html.text, parser)

	select_element = tree.xpath("//select[@id='first-choice']")[0]
	options = select_element.xpath("./option")

	result = {}

	for option in options:
	    code = option.get('value')
	    name = option.text
	    result[code] = name

	bus_data.append(result)

print(bus_data)

data_formatted = json.dumps(bus_data)

#print(f'Bus data: {data_formatted}')

with open('bus_data_scrapped.json', 'w') as f:
	f.write(data_formatted)
