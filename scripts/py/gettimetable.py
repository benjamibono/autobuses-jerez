import json
from timetable_downloader import download_timetable



report = {
	'total_bus_stops': 0,
	'download_errors_count': 0,
	'download_errors_info': [],
}


with open('bus_data.json', 'r') as f:
	
	json_data = json.loads(f.read())

	total_bus_stops = 0
	for bus_line in json_data:
		for bus_stop in bus_line['busStops']:
			total_bus_stops += 1

	report['total_bus_stops'] = total_bus_stops

	# Download timetables loop
	current_bus_stop = 0
	for bus_line in json_data:
		for bus_stop in bus_line['busStops']:
			current_bus_stop += 1
			print(f'Descargando horario {current_bus_stop} de {total_bus_stops}')
			ok = download_timetable(bus_line['id'], bus_stop['code'])
			if not ok:
				report['download_errors_count'] += 1
				report['download_errors_info'].append(f"{bus_line['id']}-{bus_stop['code']}")

	print(f'DESCARGA FINALIZADA{report}')
