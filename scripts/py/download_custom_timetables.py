from timetable_downloader import download_timetable


timetables = [
	"8-35"
]

for timetable in timetables:
	line, bus_stop = timetable.split("-")
	ok = download_timetable(line, bus_stop)