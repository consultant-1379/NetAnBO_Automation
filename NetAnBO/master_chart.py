import os
import shutil
import sys

#tesseract = sys.argv[1]
bo_list = []
netan_list = []
# for entry in os.listdir(os.getcwd()+"/BO"):
	# bo_list.append(entry)

for entry in os.listdir("NetAnBO\\NetAn"):
	netan_list.append(entry)
	
for netan in netan_list:
	#print('python missing_kpi_chart.py '+tesseract+"' BO\\"+bo+"' '"+'NetAn\\'+netan+"'")
    os.system('python NetAnBO\\missing_kpi_chart.py NetAnBO\\NetAn\\'+netan)
	
# for entry in os.listdir("NetAnBO\\NetAn"):
	# shutil.rmtree("NetAnBO\\NetAn\\"+entry)

# for entry in os.listdir("NetAnBO\\BO"):
	# os.remove("NetAnBO\\BO\\"+entry)