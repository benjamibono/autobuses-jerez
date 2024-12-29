import re
import json
import os
from timetable_downloader import download_timetable

report = {
	'missing_files': [],
	'download_errors_count': 0,
	'download_errors_info': [],
}

with open('bus_data.json', 'r') as f:
	
	json_data = json.loads(f.read())

	total_bus_stops = 0
	for bus_line in json_data:
		for bus_stop in bus_line['busStops']:
			line = bus_line['id']
			bus_stop = bus_stop['code']
			file = f"L{line}-P{bus_stop}.html"
			if not os.path.exists(f"timetables/{file}"):
				report['missing_files'].append({'line': line, 'bus_stop': bus_stop})

	count = len(report['missing_files'])
	print(f"Missing files: {count}")

	index = 1

	for file_data in report['missing_files']:
		print(f'Descargando horario {index} de {count}')
		download_timetable(file_data['line'], file_data['bus_stop'])	
		index += 1


