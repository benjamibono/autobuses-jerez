import json
import pyperclip

data = pyperclip.paste()
data_json = json.loads(data)

lines_data = {}

for line in data_json:
	lines_data[int(line["id"])] = line["description"]

pyperclip.copy(json.dumps(lines_data))

