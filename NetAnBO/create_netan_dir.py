import os

bo_list = []

# if not os.path.exists("NetAn"):
	# os.mkdir("NetAn")
if not os.path.exists("NetAnBO\\Missing KPI"):
	os.mkdir("NetAnBO\\Missing KPI")
if not os.path.exists("NetAnBO\\BO"):
	print("BO folder is not present")

#os.chdir("BO")
for entry in os.listdir("NetAnBO\\BO"):
	os.rename("NetAnBO\\BO\\"+entry,"NetAnBO\\BO\\"+entry.replace(" ",""))

for entry in os.listdir("NetAnBO\\BO"):
	bo_list.append(entry)

#os.chdir("..\\NetAn")
	
for csvs in bo_list:
	csvs = csvs.replace(" ","")
	os.mkdir("NetAnBO\\NetAn\\"+csvs[:-4])