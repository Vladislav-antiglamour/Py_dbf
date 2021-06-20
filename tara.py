import xlrd, xlwt
import os
import re
import dbf
from xlwt import *
import datetime
date=str(datetime.date.today())
                           
p_s=0
NoneType = type(None)
def set_style(name, height, bold=False, center=True):
    style = xlwt.XFStyle()  # ?????

    font = xlwt.Font()  # ???????
    font.name = name  # 'Times New Roman'
    font.bold = False
    font.color_index = 0
    font.height = height

    borders= xlwt.Borders()
    borders.left= 6
    borders.right= 6
    borders.top= 6
    borders.bottom= 6

    style.font = font
    style.borders = borders
    alignment = xlwt.Alignment()
    alignment.horz = xlwt.Alignment.HORZ_CENTER
    alignment.vert = xlwt.Alignment.VERT_CENTER
    if center == True:
        style.alignment = alignment
    else:
        style.alignment = left
    
    return style

print('МИНУТОЧКУ...')
db_tpr=dbf.Table("f:\Data\TPR.DBF")
db_tpr.open()


tara= xlrd.open_workbook('sm21.xls',formatting_info=True)
tara_ost=xlwt.Workbook()
list_tar=tara.sheet_by_index(0)
list_ost=tara_ost.add_sheet('ostat')
tara_pod=xlwt.Workbook()
list_pod=tara_pod.add_sheet('подсчет к писанию')
list_pod.portrait=False
list_ost.portrait=False
kod=[]
for row_index in range(list_tar.nrows):
    kod.append(list_tar.row_values(row_index)[0])

slovnazv={}

nazv=[]
for row_index in range(list_tar.nrows):
    nazv.append(list_tar.row_values(row_index)[1])

kod=[]
for row_index in range(list_tar.nrows):
    if type(list_tar.row_values(row_index)[0]) is float:
        kod.append(int(list_tar.row_values(row_index)[0]))
k=2
for i in kod:
    slovnazv.update({i:nazv[k]})
    k=k+1
list_ost.write(0,0, "КОД",set_style('Times New Roman',280,True,True))
list_ost.col(0).width = 5000
list_ost.write(0,1, "НАИМЕНОВАНИЕ",set_style('Times New Roman',280,True,True))
list_ost.col(1).width = 11600
list_ost.write(0,2, "ОСТАТОК",set_style('Times New Roman',280,True,True))
list_ost.col(2).width = 5000
list_ost.write(0,3, "ФАКТ",set_style('Times New Roman',280,True,True))
list_ost.col(3).width = 5000
list_ost.write(0,4, "ЗАЯВКА",set_style('Times New Roman',280,True,True))
list_ost.col(4).width = 5000
list_pod.write(0,0, "КОД",set_style('Times New Roman',280,True,True))
list_pod.col(0).width = 5000
list_pod.write(0,1, "НАИМЕНОВАНИЕ",set_style('Times New Roman',280,True,True))
list_pod.col(1).width = 11600
list_pod.write(0,2, "ОСТАТОК",set_style('Times New Roman',280,True,True))
list_pod.col(2).width = 5000
list_pod.write(0,3, "ВВЕДИ ФАКТ",set_style('Times New Roman',280,True,True))
list_pod.col(3).width = 8000
list_pod.write(0,4, "СПИСАТЬ",set_style('Times New Roman',280,True,True))
list_pod.col(4).width = 5000

i=1
j=2
for key in slovnazv:
    list_ost.write(i,0,key,set_style('Times New Roman',280,True,True))
    list_ost.write(i,1,slovnazv[key],set_style('Times New Roman',280,True,True))
    list_pod.write(i,0,key,set_style('Times New Roman',280,True,True))
    list_pod.write(i,1,slovnazv[key],set_style('Times New Roman',280,True,True))
    list_pod.write(i,3,' ',set_style('Times New Roman',280,True,True))
    forms1="C"+str(j)+"-D"+str(j)
    list_pod.write(i,4, Formula(forms1),set_style('Times New Roman',280,True,True))
    i=i+1
    j=j+1
slov_ost={}
def record_indexer(record):
    if isinstance(record.tc_, NoneType):
        return dbf.DoNotIndex             # record is ignored
    return record.tc_
index = db_tpr.create_index(record_indexer)



for key in kod:
    for rec_db in index.search(match=(key,)):
        slov_ost[key]=slov_ost.get(key,0)+rec_db[18]
i=1
for key in kod:
    if key in slov_ost:
        list_ost.write(i,2,slov_ost[key],set_style('Times New Roman',280,True,True))
        list_pod.write(i,2,slov_ost[key],set_style('Times New Roman',280,True,True))
    else:
        list_ost.write(i,2,0,set_style('Times New Roman',280,True,True))
        list_pod.write(i,2,0,set_style('Times New Roman',280,True,True))
    list_ost.write(i,3,' ',set_style('Times New Roman',280,True,True))
    list_ost.write(i,4,' ',set_style('Times New Roman',280,True,True))
    i=i+1
list_ost.write(i,2,'Должность',set_style('Times New Roman',280,True,True))
list_ost.write(i,3,'Дата',set_style('Times New Roman',280,True,True))
list_ost.write(i,4,'Подпись',set_style('Times New Roman',280,True,True))
list_ost.write(i+1,2,' ',set_style('Times New Roman',280,True,True))
list_ost.write(i+1,3,date,set_style('Times New Roman',280,True,True))
list_ost.write(i+1,4,' ',set_style('Times New Roman',280,True,True))
    
    
tara_ost.save('tara_ost.xls')
os.startfile('tara_ost.xls',"print")
tara_pod.save('tara_pod.xls')
db_tpr.close()


