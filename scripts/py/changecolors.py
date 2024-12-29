import json

colors_lines_jerez = {
	"1":  "#FFD400",
    "2":  "#f33600",
    "3":  "#e9ac14",
    "4":  "#c5013a",
    "5":  "#991e4f",
    "6":  "#bd9600",
    "7":  "#6d9000",
    "8":  "#007e80",
    "9":  "#00609d",
    "10": "#8356c4",
    "11": "#df9fc3",
    "12": "#b15215",
    "13": "#00adb3",
    "14": "#d13866",
    "15": "#232f5c",
    "16": "#b5be03",
    "17": "#752315",
    "18": "#00e0f4",
}

with open('bus_lines_data.json') as f:
	json_data = json.loads(f.read())

	for bus_line in json_data:
		bus_line['colorHex'] = colors_lines_jerez[str(bus_line['id'])]

data_json = json.dumps(json_data, indent=4)

import pyperclip
pyperclip.copy(data_json)
