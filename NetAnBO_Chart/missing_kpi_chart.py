import fitz
import os
import glob
import pytesseract
import sys

tesseract = sys.argv[1]
BO_file = sys.argv[2]
NetAn = sys.argv[3]
#pytesseract.pytesseract.tesseract_cmd = r'C:\Users\zmudshu\AppData\Local\Programs\Tesseract-OCR\tesseract'
pytesseract.pytesseract.tesseract_cmd = sys.argv[1]+'\\tesseract'
cwd = os.getcwd()

def chart_count_bo(file):
	os.chdir(cwd)
	count = 0
	xref_list = []
	doc = fitz.open(file)
	for i in range(len(doc)):
		for img in doc.getPageImageList(i):
			xref = img[0]
			xref_list.append(xref)
	xref_list = set(xref_list)
	for xref in xref_list:
		if xref > 9:
			count = count + 1
	os.chdir(cwd)
	return count

def pdf_to_img():
	os.chdir(cwd+"\\"+NetAn)
	count = 0
	for file in os.listdir(os.getcwd()):
		if file.endswith(".pdf"):
			doc = fitz.open(file)
			for i in range(len(doc)):
				for img in doc.getPageImageList(i):
					xref = img[0]
					pix = fitz.Pixmap(doc, xref)
					if pix.n < 5:       # this is GRAY or RGB
						pix.writePNG(cwd+"\\Images\\"+file+"-%s-%s.png" % (i, xref))
					else:               # CMYK: convert to RGB first
						pix1 = fitz.Pixmap(fitz.csRGB, pix)
						pix1.writePNG(cwd+"\\Images\\"+file+"-%s-%s.png" % (i, xref))
						pix1 = None
					pix = None
					count = count + 1
		
	os.chdir(cwd)
	return count

def img_string_to_file():
	name = BO_file.split("\\")[1]
	f = open("Missing KPI\\"+name+"_Missing_KPI.txt",'w+')
	f.writelines("Missing KPI from NetAn charts\n")
	os.chdir(cwd+"\\Images")
	for file in os.listdir(os.getcwd()):
		text = pytesseract.image_to_string(file)
		text = text.strip()
		text = text.replace("\n","")
		if "Could not find column" in text:
			KPI = text[text.index(":")+1:-1]
			name = file[:file.index(".pdf")]
			print(name+" - "+KPI)
			f.writelines(name+" - "+KPI+"\n")
	f.close()
	os.chdir(cwd)

def cleanup():
	for entry in os.listdir(cwd+"\\Images"):
		os.chdir(cwd+"\\Images")
		os.remove(entry)
	os.chdir(cwd)
		
netan_chart_count = pdf_to_img()
bo_chart_count = chart_count_bo(BO_file)
print(netan_chart_count)
print(bo_chart_count)
name = BO_file.split("\\")[1]
img_string_to_file()
f = open("Missing KPI\\"+name+"_Missing_KPI.txt",'a')
f.writelines("\n\n\nTotal charts in BO - "+str(bo_chart_count)+"\n")
f.writelines("Total charts in NetAn - "+str(netan_chart_count)+"\n")
f.writelines("Missing charts from NetAn - "+str(bo_chart_count-netan_chart_count))
f.close()
cleanup()


	
	
	