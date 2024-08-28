import os
import shutil
import sys
import time

node = sys.argv[1]
dxp = sys.argv[2]
dxp_new = dxp.replace(" ","")
os.rename(dxp, dxp_new)
name_list = []

def cleanup():
    os.remove("ReportsBO.csv")
    os.remove("QueryBO.csv")
    os.remove("VariablesBO.csv")
    
os.mkdir("NetAnBO\\BO")
os.mkdir("NetAnBO\\NetAn")
os.mkdir("NetAnBO\\Missing KPI")
os.mkdir("NetAnBO\\Images_Chart")
	
	
for item in os.listdir(node):
    if "Prompt" in item:
        os.remove(node+"\\"+item)
    
for item in os.listdir(node):
    if "QueryBO" in item:
        name = item[7:-4]
        if "Description" not in name:
            name_list.append(name+".csv")
    

for name in name_list:
	shutil.copy(node+"\\QueryBO"+name,'.')
	shutil.copy(node+"\\ReportsBO"+name,'.')
	shutil.copy(node+"\\VariablesBO"+name,'.')
	try:
		os.system('python test.py '+'"'+dxp_new+'"')
		time.sleep(8)
		cleanup()
	except Exception as e:
		print("Exception:")
		print(e)
		os.rename(dxp_new,dxp)
		exit()

os.rename(dxp_new,dxp)
for item in os.listdir(node):
    if "ReportsBO" in item:
        shutil.copy(node+"\\"+item,"NetAnBO\\BO")
        
for item in os.listdir("NetAnBO\\BO"):
    if "Description" in item:
        os.remove("NetAnBO\\BO\\"+item)
    else:
        os.rename("NetAnBO\\BO\\"+item,"NetAnBO\\BO\\"+item[9:])

os.system('python NetAnBO\\create_netan_dir.py')
for item in os.listdir("NetAnBO\\BO"):
    os.system('copy '+'"'+item[:-4]+'" '+'"NetAnBO\\NetAn\\'+item[:-4]+'"')

os.system("python NetAnBO\\master.py")
os.system("python NetAnBO\\master_chart.py")
 
