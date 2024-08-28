import os

bo_list = []

if not os.path.exists("NetAn"):
	os.mkdir("NetAn")
if not os.path.exists("Missing KPI"):
	os.mkdir("Missing KPI")
if not os.path.exists("BO"):
	print("BO folder is not present")

os.chdir("BO")
for entry in os.listdir(os.getcwd()):
	os.rename(entry,entry.replace(" ",""))

for entry in os.listdir(os.getcwd()):
	bo_list.append(entry)

os.chdir("..\\NetAn")
	
for csvs in bo_list:
	csvs = csvs.replace(" ","")
	os.mkdir(csvs)