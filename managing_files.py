import csv

lat_long_airbnb = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
lat_long_ayto = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
lat_long_neighborhoods = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
statistics = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

with open('data-airbnb.csv','rb') as r1:
	reader1 = csv.reader(r1,delimiter=';')
	next(reader1, None)
	for row in reader1:
		try:
			lat_long_airbnb[int(row[0])].append([float(row[3]),float(row[4])])
		except ValueError:
			print("No flats in that neighborhood!!")

with open('bcn-ayuntamiento-apts-latlong.csv','rb') as r2:
	reader2 = csv.reader(r2,delimiter=';')
	for row in reader2:
		try:
			lat_long_ayto[int(row[0])].append([float(row[2]),float(row[3])])
		except ValueError:
			print("No registered flats in that neighborhood!!")		


with open('bcn-geodata-barris.csv','rb') as r3:
	reader3 = csv.reader(r3,delimiter=';')
	for row in reader3:
		lat_long_neighborhoods[int(row[0])].append([float(row[2]),float(row[3])])

with open('registered_airbnb.csv','rb') as r4:
	reader4 = csv.reader(r4,delimiter=';')
	next(reader4, None)
	for row in reader4:
		statistics[int(row[0])].append(row[1])
		statistics[int(row[0])].append(row[8])
		statistics[int(row[0])].append(row[9])
		statistics[int(row[0])].append(row[10])
		statistics[int(row[0])].append(row[11])

flag_lat_long_airbnb = "var inside_airbnb =" 
flag_lat_long_ayto = "var registered_flats ="
flag_neighborhoods = "var neighborhoods_list ="
flag_statistics = "var statistics ="

#searchs for the flag in html file and writes the array right after it
with open('data_representation_alert.html','r+') as l1:
	lines = l1.readlines()
	l1.seek(0)
	l1.truncate()
	for line in lines:
		if line.startswith(flag_lat_long_airbnb):
			line = line.rstrip("\n") + str(lat_long_airbnb) + "\n"
		l1.write(line)


with open('data_representation_alert.html','r+') as l2:
	lines = l2.readlines()
	l2.seek(0)
	l2.truncate()
	for line in lines:
		if line.startswith(flag_lat_long_ayto):
			line = line.rstrip("\n") + str(lat_long_ayto) + "\n"
		l2.write(line)


with open('data_representation_alert.html','r+') as l3:
	lines = l3.readlines()
	l3.seek(0)
	l3.truncate()
	for line in lines:
		if line.startswith(flag_neighborhoods):
			line = line.rstrip("\n") + str(lat_long_neighborhoods) + "\n"
		l3.write(line)


with open('data_representation_alert.html','r+') as l4:
	lines = l4.readlines()
	l4.seek(0)
	l4.truncate()
	for line in lines:
		if line.startswith(flag_statistics):
			line = line.rstrip("\n") + str(statistics) + "\n"
		l4.write(line)

			
