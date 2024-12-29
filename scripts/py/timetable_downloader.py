import json
from lxml import etree
from lxml.html.soupparser import fromstring
import requests

def clean_html(html_text):

	# fix for nested frames
	#html_text = html_text.replace('<div style="width: 100px; float: left;"/>', '')

	try:
		root = fromstring(html_text)
		timetable = root.xpath('//div[@class="section section-default"]')[0]
		timetable_code = str(etree.tostring(timetable), "utf-8")
		timetable_code = timetable_code.replace("", "").replace("\t", "")
		timetable_code = timetable_code.replace('<div style="width: 30%; border: 1px solid black; float: left; padding: 10px; margin: 10px;"><strong>S&#225;bados</strong>', '</div><div style="width: 30%; border: 1px solid black; float: left; padding: 10px; margin: 10px;"><strong>S&#225;bados</strong>')
		return timetable_code
	except Exception as e:
		print("EXCEPTION: " + str(e))
		return html_text


def download_timetable(line_number, bus_stop_code):

	print(f'linea{line_number}-parada{bus_stop_code}')

	payload = {'valorLinea': line_number, 'valorCaja1': bus_stop_code}
	r = requests.post("https://www.comujesa.es/autobuses-urbanos/paradas-y-horarios/listar-b", data=payload)

	if r.status_code == requests.codes.ok:x

	html_str = r.text

		# Detect empty times (means bad timetable request)
	empty_times_count = html_str.count("<div style='width: 100px; float: left;'></div>")
	if empty_times_count == 3:
		print(f'error. empty timetable L{line_number}-P{bus_stop_code}')
		return False

	html_cleaned = clean_html(html_str)

	with open(f'timetables/L{line_number}-P{bus_stop_code}.html', 'w') as file_out:
		file_out.write(html_cleaned)

	return True

	print(f'error downloading L{line_number}-P{bus_stop_code}')
	return False