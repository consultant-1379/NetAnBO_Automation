import os
import shutil
import sys

tesseract = sys.argv[1]
bo_list = []
netan_list = []
for entry in os.listdir(os.getcwd()+"/BO"):
	bo_list.append(entry)

for entry in os.listdir(os.getcwd()+"/NetAn"):
	netan_list.append(entry)
	
for bo,netan in zip(bo_list,netan_list):
	print('python missing_kpi_chart.py '+tesseract+"' BO\\"+bo+"' '"+'NetAn\\'+netan+"'")
	os.system('python missing_kpi_chart.py '+tesseract+' BO\\'+bo+' NetAn\\'+netan)
	
for entry in os.listdir(os.getcwd()+"/NetAn"):
	shutil.rmtree("NetAn/"+entry)

for entry in os.listdir(os.getcwd()+"/BO"):
	os.remove("BO/"+entry)