import dbf
import datetime
import os
maszak_ras=[]
dict_pri_ras={}
num_zak_ras=0
proc=0
otk=0
itog=0
itog_syr=0
#cur_date=datetime.datetime.now()
db_tpr=dbf.Table("f:\data\TPR.DBF")
db_tpr.open()
db_tra=dbf.Table("f:\data\TRA.DBF")
db_tra.open()
db_ras=dbf.Table("f:\data\RAS.DBF")
db_ras.open()
db_pri=dbf.Table("f:\data\PRI.DBF")
db_pri.open()
otch=open('полный отчет.txt','w')
print('Введите месяц за который отчет делаем \n')
cur_date=int(input())
#заполнение массива номерами расходов на гриль
print('Готовлю данные жди \n')

for rec_date in db_ras:
    if rec_date.rp_.month==cur_date and rec_date.rc_==585:
        maszak_ras.append(rec_date.ra_)
       
print(maszak_ras)

#заполнение словаря приходов на основании расходов

for i in maszak_ras:
    dict_pri_ras.setdefault(i,[])
    for rec_zak in db_pri:
        string=str(rec_zak.pb_).split()
        string=''.join(string)
        if string==str(i):
            dict_pri_ras[i].append(rec_zak.pa_)


          
            
num_zak_ras=[]
print('Введи номер пследней хакрытой партии КУРЕЙ ГРИЛЬ(номер расхода) нажми ентер:\n')
num_zak_ras.append(input())
print('Введи номер послежней хакрытой партии ОКОРОЧКОВ ГРИЛЬ(номер расхода) нажми ентер:\n')
num_zak_ras.append(input())
print('Введи номер послежней хакрытой партии КРЫЛЬЕВ ГРИЛЬ(номер расхода) нажми ентер:\n')
num_zak_ras.append(input())

print('жди...\n')


  

otch.write('____________КУРЫ ГРИЛЬ______________\n')
otch.write('\n')
otch.write('\n')              

for rec in db_tpr:
    for key,val in dict_pri_ras.items():
        
        if key<=int(num_zak_ras[0]):
            
            for i in dict_pri_ras[key]:
                
            
                if rec.ta_==i and rec.tc_==2280303:
                    
                    otch.write('Готовые куры гриль            '+str(rec.ti_)+'\n')
                    itog+=rec.ti_

otch.write('++++++++++++++++++++++++++++++++++++++++++++++++++\n')
otch.write('Итоговое значение по готовым курям(2280303):   '+"%.2f"%itog+'\n')



for key,val in dict_pri_ras.items():
    for rec in db_tra:
        if key<=int(num_zak_ras[0]):
            if key==rec.va_ and rec.vc_==4070001:
                
                otch.write('Сырье куры            '+str(rec.vi_)+'\n')
                itog_syr+=rec.vi_

otch.write('++++++++++++++++++++++++++++++++++++++++++++++++++\n')
otch.write('Итоговое значение по сырью куры(4070001):   '+str(itog_syr)+'\n')
otch.write('Процент выхода готовой продукции:   '+"%.2f"%((itog*100)/itog_syr)+'\n')
otch.write('Отклонение при норме 65%:    '+"%.2f"%((itog*100/itog_syr)-65))
otch.write('\n')       
otch.write('\n')
otch.write('\n')
otch.write('\n')       
otch.write('\n')
otch.write('\n')


itog=0
itog_syr=0


print('жди...\n')

otch.write('____________ОКОРОЧКА ГРИЛЬ______________\n')
otch.write('\n')
otch.write('\n')              

for rec in db_tpr:
    for key,val in dict_pri_ras.items():
        
        if key<=int(num_zak_ras[1]):
            
            for i in dict_pri_ras[key]:
                
            
                if rec.ta_==i and rec.tc_==2280304:
                    
                    otch.write('Готовые окорочка           '+str(rec.ti_)+'\n')
                    itog+=rec.ti_

otch.write('++++++++++++++++++++++++++++++++++++++++++++++++++\n')
otch.write('Итоговое значение по готовым окорочкам(2280304):   '+"%.2f"%itog+'\n')



for rec in db_tra:
    for key,val in dict_pri_ras.items():
        if key<=int(num_zak_ras[1]):
        
            if key==rec.va_ and rec.vc_==4070003:
                otch.write('Сырье окорочка            '+str(rec.vi_)+'\n')
                itog_syr+=rec.vi_
otch.write('++++++++++++++++++++++++++++++++++++++++++++++++++\n')
otch.write('Итоговое значение по сырью окорочка(4070003):   '+str(itog_syr)+'\n')
otch.write('Процент выхода готовой продукции:   '+"%.2f"%((itog*100)/itog_syr)+'\n')
otch.write('Отклонение при норме 60%:    '+"%.2f"%((itog*100/itog_syr)-60))
otch.write('\n')       
otch.write('\n')
otch.write('\n')
otch.write('\n')       
otch.write('\n')
otch.write('\n')


itog=0
itog_syr=0
otch.write('____________КРЫЛЬЯ ГРИЛЬ______________\n')
otch.write('\n')
otch.write('\n')              
for rec in db_tpr:
    for key,val in dict_pri_ras.items():
        
        if key<=int(num_zak_ras[2]):
            
            for i in dict_pri_ras[key]:
                
            
                if rec.ta_==i and rec.tc_==2280305:
                    
                    otch.write('Готовые крылья            '+str(rec.ti_)+'\n')
                    itog+=rec.ti_

otch.write('++++++++++++++++++++++++++++++++++++++++++++++++++\n')
otch.write('Итоговое значение по готовым курям(2280305):   '+"%.2f"%itog+'\n')



for rec in db_tra:
    for key,val in dict_pri_ras.items():
        if key<=int(num_zak_ras[2]):
        
            if key==rec.va_ and rec.vc_==4070002:
                otch.write('Сырье крылья            '+str(rec.vi_)+'\n')
                itog_syr+=rec.vi_
otch.write('++++++++++++++++++++++++++++++++++++++++++++++++++\n')
otch.write('Итоговое значение по сырью крылья(4070002):   '+str(itog_syr)+'\n')
otch.write('Процент выхода готовой продукции:   '+"%.2f"%((itog*100)/itog_syr)+'\n')
otch.write('Отклонение при норме 66%:    '+"%.2f"%((itog*100/itog_syr)-66))
otch.write('\n')       
otch.write('\n')
otch.write('\n')
otch.write('\n')       
otch.write('\n')
otch.write('\n')


itog=0
itog_syr=0
'''
otch.write("_____________НАЙДЕНЫЕ КОСЯКИ!!!________\n")
otch.write('\n')
mas_rah_gril=[]
mas_prih_gril=[]
maskodras=[4070001,4070002,4070003]
maskodpri
for i in maskodras:
    for g in index_ras.search(match=i):
        mas_rah_gril.append(g[0])

otch.write('В этих расходах неправилно указан поствщик:\n')
otch.write('\n')
index_numras=db_ras.create_index(key=lambda rec:rec.ra_)
for i in mas_rah_gril:
    for j in index_numras.search(match=i):
        if  j[2]!=585:
            otch.write(str(j[0])+' :указан '+ str(j[2])+' должен быть 585\n')

maskodpri=[2280303,2280304,2280305]
for i in maskodpri:
    for j in index_pri.search(match=i):
         
            mas_prih_gril.append(j[0])
      

otch.write('в этих приходах неправильно указан поставщик:\n')
otch.write('\n')

for i in mas_prih_gril:
    for j in db_pri:
        if j[0]==i and j[3]!=595:
            otch.write('Приход № '+str(j[0])+'указан:  '+str(j[2])+' нужно 595\n')

count=0
 
for i in mas_rah_gril:
    
    for j in db_pri:
        string=str(j[1]).split()
        string=''.join(string)
        
        if string==str(i):
            count+=1
    if count==0:
        otch.write('по номеру документа поставщика(расхода): '+str(i)+' не найдено не одного прихода с грилем\n')
        
    count=0 
      

for i in mas_prih_gril:
    for j in db_pri:
        if j[0]==i:
            string=str(j[1]).split()
            string=''.join(string)
            if int(string) not in mas_rah_gril:
                otch.write('в приходном документе:  '+str(j[0])+' указан номер документа поставщика(расхода) в котром нет сырья')
otch.write('\n')
otch.write('Если есть косяки исправь  и запусти программу заново\n')
        
#count=len(mas_rah_gril)
#for i in mass_nudoc:
 #   if i
otch.write('\n')
otch.write('\n')
otch.write('\n')
otch.write('\n')
otch.write('\n')
    
  


'''
otch.write('Отчет сформирован:  '+str(datetime.datetime.now()))
otch.close() 
os.startfile('полный отчет.txt')
db_tpr.close()
db_tra.close()
db_pri.close()
db_ras.close()
