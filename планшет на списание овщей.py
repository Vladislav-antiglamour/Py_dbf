import xlrd, xlwt
import os
import re
import dbf
from xlwt import *
import datetime
from xlutils.copy import copy
print("ван момент плиз")
p_s=0
NoneType = type(None)
date=str(datetime.date.today())
def set_style(name, height, bold=False, center=True):
    style = xlwt.XFStyle()  # ?????

    font = xlwt.Font()  # ???????
    font.name = name  # 'Times New Roman'
    font.bold = True
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
    
    return style
db_tpr=dbf.Table("f:\Data\TPR.DBF")
db_tpr.open()
db_ass=dbf.Table("f:\Data\ASS.DBF")
db_ass.open()
def record_indexer_tpr(record):
    if isinstance(record.tc_, NoneType):
        return dbf.DoNotIndex             # record is ignored
    return record.tc_
def record_indexer_ass(record):
    if isinstance(record.aa_, NoneType):
        return dbf.DoNotIndex             # record is ignored
    return record.ab_
slovar_ass={}
slovar_ost={}
index_ass=db_ass.create_index(record_indexer_ass)
index_tpr=db_tpr.create_index(record_indexer_tpr)
for rec_ass in index_ass.search(match=(605,)):
    slovar_ass[rec_ass[0]]=slovar_ass.get(rec_ass[0],'')+rec_ass[2]
for rec_ass in index_ass.search(match=(606,)):
    slovar_ass[rec_ass[0]]=slovar_ass.get(rec_ass[0],'')+rec_ass[2]
for key in slovar_ass.keys():
    for rec_tpr in index_tpr.search(match=(key,)):
        slovar_ost[key]=slovar_ost.get(key,0)+rec_tpr[18]
arr_605=[]
arr_606=[]
for key in slovar_ost.keys():
    if key//10000==605 and slovar_ost[key]>0:
        arr_605.append(key)
    elif key//10000==606 and slovar_ost[key]>0:
        arr_606.append(key)
arr_605.sort()
arr_606.sort()
plansh= xlrd.open_workbook('СПИСАНИЕ огорода - копия.xls',formatting_info=True)
plansh_cop=copy(plansh)
plansh_cop_sheet = plansh_cop.get_sheet(0)
plansh_cop_sheet.print_scaling=83
plansh_cop_sheet.left_margin=0.4
plansh_cop_sheet.top_margin=0
plansh_cop_sheet.right_margin=0
plansh_cop_sheet.bottom_margin=0
i=3
for key in arr_605:
    plansh_cop_sheet.write(i,0,key,set_style('Calibri',239,True,False))
    plansh_cop_sheet.write(i,1,slovar_ass[key],set_style('Calibri',239,True,False))
    
    i=i+1
i=57
for key in arr_606:
    plansh_cop_sheet.write(i,0,key,set_style('Calibri',239,True,False))
    plansh_cop_sheet.write(i,1,slovar_ass[key],set_style('Calibri',239,True,False))
    i=i+1
    
plansh_cop.save('ovoshi.xls')
os.startfile('ovoshi.xls')
db_tpr.close()
db_ass.close()
#os.startfile('ovoshi.xls',"print")
