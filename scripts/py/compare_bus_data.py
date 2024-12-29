import json

lines_comparation = []

with open('bus_data.json', 'r') as f:
	with open('bus_data_scrapped.json', 'r') as f2:
		
		json_data_local = json.loads(f.read())
		json_data_scrapped = json.loads(f2.read())

		bus_line_numbers = list(range(1, 19))

		for bus_line_number in bus_line_numbers:

			bus_line = json_data_local[bus_line_number-1]
			bus_line_2 = json_data_scrapped[bus_line_number-1]

			old = []
			for bus_stop in bus_line['busStops']:
				line = bus_line['id']
				bus_stop_code = str(bus_stop['code'])
				bus_stop_name = bus_stop['name']

				if not bus_stop_code in bus_line_2:
					old.append(f"{bus_stop_name} ({bus_stop_code})")

			new = []
			for bus_stop_code, bus_stop_name in bus_line_2.items():
				
				if bus_stop_code == '0':
					continue

				element = next((x for x in bus_line['busStops'] if x['code'] == int(bus_stop_code)), None)
				if not element:
					new.append(f"{bus_stop_name} ({bus_stop_code})")

			lines_comparation.append({
				"old": old,
				"new": new,
				})

for index, line_comp in enumerate(lines_comparation):
	line = index + 1
	print(f"Linea {line}")
	if line_comp['old']:
		print("Antiguas: " + str(line_comp['old']))
	if line_comp['new']:
		print("Nuevas: " + str(line_comp['new']))

