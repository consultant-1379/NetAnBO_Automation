import os
import glob
import sys
import re

def BO_to_dict(BO_file):
	if not os.path.exists(BO_file):
		print(BO_file+" does not exist")
		exit()
	BO_dict = {}
	topology = "xx,xx"
	BO_file = open(BO_file,'r')
	BO_data = BO_file.readlines()
	BO_table = []
	rows = []
	columns = []
	for data in BO_data:
		if "Table" in data and "<100.00%" not in data:
			BO_table.append(data)
		if "<100.00%" in data:
			topology = data
		
			
	for table in BO_table:
		table = table.strip()
		rows = table.split("Table,")
		for row in rows:
			row = row.strip()
			#row = row.replace("\'","")
			columns.append(row)
	
	types = columns[0::2]
	KPI_type = []
	for type in types:
		type = type.split(",")[1]
		KPI_type.append(type)

	KPI = columns[1::2]
	zip_iterator = zip(KPI_type, KPI)
	BO_dict = dict(zip_iterator)
	BO_file.close()
	return BO_dict, topology
	
def combine_netan_csv(NetAn_fold, topology, BO_dict):
	if not os.path.exists(NetAn_fold):
		print(NetAn_fold+" folder does not exist")
		exit()
	#read_files = glob.glob(NetAn_fold+"\*.csv")
	read_files = BO_dict.keys()
	print(read_files)
	NetAn_csv = "NetAnBO\\NetAn.csv"
	top = topology.split(',')[1]
	with open(NetAn_csv, "w") as outfile:
		for f in read_files:
			if top not in f:
				with open(NetAn_fold+"\\"+f+".csv", "r", encoding="utf-16") as infile:
					outfile.write(infile.readline())
					if infile.readline() == "":
						outfile.write("\n")
				#outfile.write("\n")
	if os.path.exists("NetAnBO\\NetAn.csv"):
		return NetAn_csv
		
def NetAn_KPI_list(NetAn_fold, topology, BO_dict):
	KPI=[]
	if not os.path.exists(NetAn_fold+"\\error.txt"):
		NetAn_csv = combine_netan_csv(NetAn_fold, topology, BO_dict)
		f = open(NetAn_csv,'r')
		for line in f.readlines():
			line = line.strip()
			KPI.append(line)
	return KPI
	
BO_file = sys.argv[1]
NetAn_folder = sys.argv[2]
name = NetAn_folder.split("\\")[2]
BO_dict, topology = BO_to_dict(BO_file)
BO_KPI = []
KPI = NetAn_KPI_list(NetAn_folder, topology, BO_dict)
NetAn_KPI = []
values = []

for val in BO_dict.values():
	val = val.strip()
	# if "ERBS" in BO_file:
		# values = val.split(", ")
	# else:
		# values = val.split(",")
	# print(values)
	if "3'" in val or "2'" in val:
		values = re.findall("\"(.*?)\"",val)
	else:
		values = re.findall("\'(.*?)\'",val)
	# if "ERBS" in BO_file:
		# values = values[5:]
	if "Time" in values:
		values = values[values.index("Time")+1:]
	val_str = '|'.join(values)
	BO_KPI.append(val_str)
if KPI:
	for val in KPI:
		groups = val.split(',')
		if "Time" in groups:
			val = '|'.join(groups[2:])
		else:
			val = '|'.join(groups)
		NetAn_KPI.append(val)
	
BO_KPI = [x.replace('"','') for x in BO_KPI]
BO_KPI = list(filter(None, BO_KPI))
BO_KPI = [x.upper() for x in BO_KPI]
print("\n"+name+"BO-KPI:")
print(BO_KPI)
#NetAn_KPI = NetAn_KPI.sort()
print("\n"+name+"NetAn-KPI:")
print(NetAn_KPI)
#name = BO_file.split("\\")[2]
if len(BO_KPI) > len(NetAn_KPI):
	while len(BO_KPI) != len(NetAn_KPI):
		NetAn_KPI.append("xx")

if NetAn_KPI:
    file = open("NetAnBO\\Missing KPI\\MissingKPI"+name+".csv",'w+')
    print("\n"+name+"Missing KPIs:")
    for BO,NetAn in zip(BO_KPI,NetAn_KPI):
        x = BO.split("|")
        y = NetAn.split("|")
        missing_kpi = list(set(x)-set(y))
        print(missing_kpi)
        file.write(str(missing_kpi)+"\n")
    file.close()
if not NetAn_KPI:
	file = open("NetAnBO\\Missing KPI\\MissingKPI"+name+".csv",'w+')
	for kpi in BO_KPI:
		file.write(kpi+" ")
	file.close()
	
	
	