import os
import pyautogui
import time
import shutil
import pytesseract
import sys

dxp = sys.argv[1]
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

for item in os.listdir():
    if item.endswith(".csv"):
        if 'Query' in item:
            if not os.path.exists(item[7:-4].replace(" ","")):
                os.mkdir(item[7:-4].replace(" ",""))
            folder = item[7:-4].replace(" ","")

for item in os.listdir():
	if item.endswith(".csv"):
		if 'Query' in item:
			os.rename(item, item[0:7]+".csv")
		if "Reports" in item:
			os.rename(item, item[0:9]+".csv")
		if "Variables" in item:
			os.rename(item, item[0:11]+".csv")
			
f = open("ReportsBO.csv",'r')
lines = f.readlines()
count = len(lines) - 1


def check_pdf():
    im = pyautogui.screenshot(region=(50,50, 900, 550))
    file = r"Images\\chart.png"
    im.save(file)
    text = pytesseract.image_to_string(file)
    text = text.strip()
    text = text.replace("\n","")
    if "Chart" in text:
        return True
    return False

def copy_file(folder):
	for item in os.listdir():
		if item.endswith(".csv") or item.endswith(".pdf"):
			if not item.endswith("BO.csv"):
				shutil.copy(item,folder)
				os.remove(item)

def export_csv(folder, i):
	pdf = check_pdf()
	i = str(i)
	pyautogui.click(file)
	pyautogui.click(export)
	if pdf:
		pyautogui.click(to_pdf)
		time.sleep(2)
		pyautogui.click(current_page)
		time.sleep(2)
		pyautogui.click(portrait)
		time.sleep(2)
		pyautogui.click(fit_pdf)
		time.sleep(2)
		pyautogui.click(export_pdf)
		time.sleep(4)
		pyautogui.click(save_path_pdf); pyautogui.write("C:\\jenkins\\workspace\\NetAn_BO_Test\\NetAnBO_Automation\\"); pyautogui.press('enter')
		time.sleep(2)
		pyautogui.doubleClick(save_box_pdf)
		pyautogui.typewrite(['C','h','a','r','t',i])
		time.sleep(2)
		pyautogui.press('enter')
		time.sleep(10)
		pyautogui.click(close1)
	else:
		pyautogui.click(data_file)
		time.sleep(2)
		pyautogui.click(ok2)
		time.sleep(4)
		#pyautogui.click(save)
		pyautogui.click(save_path); pyautogui.write("C:\\jenkins\\workspace\\NetAn_BO_Test\\NetAnBO_Automation\\"); pyautogui.press('enter')
		time.sleep(2)
		pyautogui.doubleClick(save_box)
		pyautogui.press('enter')
		time.sleep(10)
	copy_file(folder)
	pyautogui.click(select_page)
	time.sleep(5)

def click_count(count, folder):
    x = 1227
    y = 710
    i = 0
    while count > 0:
        pyautogui.click(x, y)
        time.sleep(2)
        export_csv(folder, i)
        y = y - 20
        count = count - 1
        i = i + 1
        
def exit_on_error(folder):
    im = pyautogui.screenshot(region=(370,520, 600, 120))
    file = r"Images\\output_box.png"
    im.save(file)
    text = pytesseract.image_to_string(file)
    text = text.strip()
    text = text.replace("\n","")
    if "Unable to execute" in text or "ERROR" in text:
        print("\n"+folder+" Query Error")
        f = open(folder+"\\error.txt",'w+')
        f.write(text)
        f.close()
        pyautogui.click(ok)
        time.sleep(2)
        pyautogui.click(close)
        time.sleep(2)
        pyautogui.click(close1)
        time.sleep(2)
        pyautogui.click(no)
        time.sleep(5)
        #cleanup()
        exit()
        
def save_output(folder):
    output = (895,572)
    pyautogui.click(output)
    time.sleep(2)
    pyautogui.scroll(-200000)
    time.sleep(3)
    im = pyautogui.screenshot(region=(370,520, 600, 120))
    file = r"Images\\calc-output.png"
    im.save(file)
    text = pytesseract.image_to_string(file)
    text = text.strip()
    text = text.replace("\n","")
    print("\n"+folder+"BO_CalculatedColumns Output:\n")
    if "KPIs not added" in text:
        text = text[text.index("KPIs not added")+14:]
        print("KPIS not added\n")
    print(text+"\n")

num = list(range(10))		
close1 = (1332, 13)
no = (716, 453)
security_alert = (550, 415)
missing_file = (455, 415)
ok1 = (795, 462)
file = (148, 43)
manage = (222, 393)
BO_Import = (297, 95)
execut_script = (623, 490)
ok = (861, 655)
BO_Test = (298, 111)
close = (1079, 681)
#page = (955, 744)
#page = (319, 705)
table = (1266, 112)
first = (1266, 472)
BO_Merge = (301, 128)
BO_calculated = (301, 147)
BO_Chart = (269, 164)
select_page = (1214, 710)
# select_page1 = (1064, 710)
page = (1214, 710)
#last_page = (882, 753)
export = (228, 231)
data_file = (430, 297)
ok2 = (758, 511)
save = (506, 470)
drop = (1284, 706)
to_pdf = (445, 268)
current_page = (95, 173)
export_pdf = (1155, 658)
portrait = (96, 446)
fit_pdf = (96, 515)
path_box = (83, 128)
save_path = (420, 72)
save_box = (322, 401)
save_path_pdf = (487, 108)
save_box_pdf = (425, 437)

#os.chdir("C:\\Shubham")
os.system('start '+dxp)
time.sleep(3)
pyautogui.click(security_alert)
time.sleep(20)
pyautogui.click(missing_file)
time.sleep(6)
pyautogui.click(ok1)
time.sleep(10)
pyautogui.click(path_box); pyautogui.hotkey('ctrl', 'a'); pyautogui.write("C:\\jenkins\\workspace\\NetAn_BO_Test\\NetAnBO_Automation")
time.sleep(2)
pyautogui.click(file)
time.sleep(2)
pyautogui.click(manage)
time.sleep(2)
pyautogui.doubleClick(BO_Import)
time.sleep(2)
pyautogui.click(execut_script)
time.sleep(8)
pyautogui.click(ok)
time.sleep(2)
pyautogui.doubleClick(BO_Test)
time.sleep(2)
pyautogui.click(execut_script)
time.sleep(50)
exit_on_error(folder)
pyautogui.click(ok)
time.sleep(2)
pyautogui.click(close)
time.sleep(2)
# pyautogui.click(page)
# time.sleep(2)
pyautogui.click(drop)
time.sleep(2)
pyautogui.click(select_page)
time.sleep(2)
pyautogui.click(page)
time.sleep(2)
pyautogui.click(table)
time.sleep(2)
pyautogui.click(first)
time.sleep(2)
pyautogui.click(file)
time.sleep(2)
pyautogui.click(manage)
time.sleep(2)
pyautogui.doubleClick(BO_Merge)
time.sleep(2)
pyautogui.click(execut_script)
time.sleep(20)
pyautogui.click(ok)
time.sleep(2)
pyautogui.doubleClick(BO_calculated)
time.sleep(2)
pyautogui.click(execut_script)
time.sleep(10)
save_output(folder)
pyautogui.click(ok)
time.sleep(2)
pyautogui.doubleClick(BO_Chart)
time.sleep(2)
pyautogui.click(execut_script)
time.sleep(10)
pyautogui.click(ok)
time.sleep(2)
pyautogui.click(close)
time.sleep(2)
pyautogui.click(select_page)
time.sleep(2)
click_count(count, folder)
time.sleep(2)
pyautogui.click(close1)
time.sleep(2)
#pyautogui.click(no)
pyautogui.typewrite(['right', 'enter'])
time.sleep(5)
#cleanup()

