import json
import requests
from static_data import *

class BusLine:
	id = 0
	name = ''
	description = ''
	color = 0
	colorHex = ''
	busStops = []
	path = []
	finalBusStopCode = 0



class BusStop:
	name = ''
	code = 0
	lineId = 0
	transfer = ''
	direction = ''
	way = ''
	coordinates = []
	nonRegular = False




bus_lines = []



lines_files = ["1-5", "6-10", "11-14", "15-18"]

# These lines has 2 LineString
repeat_path_line_15 = True

for lines_file in lines_files:

	print(f'Procesando archivo lineas {lines_file}')

	starting_line_number = int(lines_file.split('-')[0])
	line_number = starting_line_number

	print(f'Línea de comienzo en archivo {starting_line_number}')

	file_geojson = open(f'geojson/lineas_{lines_file}.geojson', 'r+')
	geojson_text = file_geojson.read()
	geojson_text = geojson_text.replace('COD. PARADA', 'COD').replace('COD.PARADA', 'COD').replace('Codigo de parada', 'COD')
	file_geojson.close()

	geojson = json.loads(geojson_text)

	features = geojson['features']


	bus_line = BusLine()
	bus_line.path = []

	bus_stops = []

	index = 0;
	direction_index = 0

	for feature in features:

		index = index + 1

		geometry = feature['geometry']
		type_geometry = geometry['type']

		if type_geometry == 'Point':

			properties_bus_stop = feature['properties']
			bus_stop_name = properties_bus_stop['name'].strip()

			bus_stop_name_and_line_number = f'L{line_number}-{bus_stop_name}'
#			if bus_stop_name_and_line_number in fake_bus_stops:
#				continue


			bus_stop = BusStop()
			bus_stop.name = bus_stop_name
			bus_stop.lineId = line_number
			bus_stop.nonRegular = bus_stop_name in non_regular_bus_stops

			# if 'Angustias' in bus_stop_name:
			#	print(f'Angustias encontrado. nombre: {bus_stop_name} Linea: {line_number}')

			try:
				if 'COD' in properties_bus_stop:
					bus_stop.code = int(float(properties_bus_stop['COD']))
					#print(f'bus_stop.code: {bus_stop.code}')
				else:
					bus_stop.code = -1
					print('no COD')

			except:
				bus_stop.code = -1
				print(f'Code not found. Línea: {line_number}. parada: {bus_stop_name}. index: {index}')
				

			#download_timetable(line_number, bus_stop.code, bus_stop_name)

			if 'TRANSBORDO' in properties_bus_stop:
				bus_stop.transfer = properties_bus_stop['TRANSBORDO'].strip()

			#if 'SENTIDO' in properties_bus_stop:

			if line_number == 8:
				bus_stop.direction = 'Sentido antihorario'
			elif line_number == 9:
				bus_stop.direction = 'Sentido horario'
			else:
				# print(f'line_number: {line_number}, direction_index: {direction_index}')
				current_direction_data = direction_names[line_number][direction_index]
				bus_stop.direction = current_direction_data['direction']
				
				bus_stop_name_to_continue = current_direction_data['destination']
				if bus_stop.name == bus_stop_name_to_continue and direction_index == 0:
					direction_index += 1;

			coordinates = geometry['coordinates']
			bus_stop.coordinates = [float(coordinates[1]), float(coordinates[0])]

			bus_stops.append(bus_stop.__dict__)

		elif type_geometry == 'LineString':

			properties_line = feature['properties']
			bus_line.name = properties_line['name'].replace(' Regular', '')
			bus_line.id = line_number
			bus_line.finalBusStopCode = final_bus_stop_code_switcher.get(line_number)

			
			bus_line.description = bus_lines_descriptions[str(line_number)]

			coordinates_list = geometry['coordinates']


			if bus_line.path:
				print(f'Mas de un LineString en linea {line_number}. Se añadiran al anterior')

			# print(f'coordinates_list size: {len(coordinates_list)}')

			for coordinates in coordinates_list:
				bus_line.path.append([float(coordinates[1]), float(coordinates[0])])


			# After a LineString a new bus_line starts with these exceptions

			if line_number == 15 and repeat_path_line_15:
				repeat_path_line_15 = False
				continue


			bus_line.color = 0
			bus_line.colorHex = colors_lines_jerez[str(line_number)]
			bus_line.busStops = bus_stops
			bus_lines.append(bus_line)

			bus_line = BusLine()
			bus_line.path = []
			bus_stops = []

			direction_index = 0

			line_number += 1
			# print(f'Línea siguiente {line_number}')


serialized_data = json.dumps([ob.__dict__ for ob in bus_lines])
#print(serialized_data)


import pyperclip
pyperclip.copy(serialized_data)

print("Completado.Copiado al portapapeles")