import os
import shutil
bo_list = []
netan_list = []
for entry in os.listdir("NetAnBO\\BO"):
	bo_list.append(entry)

for entry in os.listdir("NetAnBO\\NetAn"):
	netan_list.append(entry)
	
for bo,netan in zip(bo_list,netan_list):
	#print('python NetAnBO\\find_missing-kpis.py '+"'NetAnBO\\BO\\"+bo+"' '"+'NetAnBO\\NetAn\\'+netan+"'")
	os.system('python NetAnBO\\find_missing-kpis.py '+'NetAnBO\\BO\\'+bo+' NetAnBO\\NetAn\\'+netan)
	
# for entry in os.listdir("NetAnBO\\NetAn"):
	# shutil.rmtree("NetAnBO\\NetAn\\"+entry)

# for entry in os.listdir("NetAnBO\\BO"):
	# os.remove("NetAnBO\\BO\\"+entry)