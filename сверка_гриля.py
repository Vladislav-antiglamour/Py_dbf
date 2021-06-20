import dbf
import datetime
import os
maszak_ras=[]
mas_pri=[]
levpos_p=[]
levpos_ras=[]
nspisrk={}
nspisrkr={}
nspisrok={}
kody_p=[2280303,2280304,2280305]
kody_ras=[4070001,4070002,4070003]
db_tpr=dbf.Table("f:\data\TPR.DBF")
db_tpr.open()
db_tra=dbf.Table("f:\data\TRA.DBF")
db_tra.open()
db_ras=dbf.Table("f:\data\RAS.DBF")
db_ras.open()
db_pri=dbf.Table("f:\data\PRI.DBF")
db_pri.open()
otch=open('sver_gril.txt','w')
print('Введите месяц за который отчет делаем \n')
kura=[]
krylo=[]
okor=[]
kura_pr={}
krylo_pr={}
okor_pr={}
cur_date=int(input())
NoneType = type(None)
p_s=0
kos_pri=[]
#заполнение массива номерами расходов на гриль
print('Готовлю данные жди \n')
for rec_date in db_ras:
    if isinstance(rec_date.rp_, NoneType):
            p_s=+1 
    elif rec_date.rp_.month==cur_date and rec_date.rc_==585:
        maszak_ras.append(rec_date.ra_)
#заполнение массива номерами приходов на гриль
for rec_date in db_pri:
    if isinstance(rec_date.ps_, NoneType):
            p_s=+1 
    elif rec_date.ps_.month==cur_date and rec_date.pn_==595:
        mas_pri.append(rec_date.pa_)

        
#функция выбора расходов гриля
def vybor_ras (kod,mas=[]):
    for rec_db in db_tra:
        if isinstance(rec_db.vc_, NoneType):
            p_s=+1 
        elif rec_db.vc_ == kod and rec_db.va_ not in mas and rec_db.va_ in maszak_ras:
            mas.append(rec_db.va_)
#функция выбора приходов на основаии раходов
def vybor_prih(mas1=[],dic={}):
    for rec in mas1:
        dic.setdefault(rec,[])
        for rec_db in db_pri:
            string=str(rec_db.pb_).split()
            string=''.join(string)
            if isinstance(rec_db.pb_, NoneType):
                p_s=+1 
            elif string == str(rec):
                dic[rec].append(rec_db.pa_)
#Функия поиска приходов с левыми реквизитами
def levrekv(mas1=[], mas2=[]):
    mas_pri_595=[]
    mas_ras_585=[]
    for rec_date in db_pri:
        if isinstance(rec_date.ps_, NoneType):
            p_s=+1 
        elif rec_date.pn_==595:
            
            mas_pri_595.append(rec_date.pa_)
    for rec_date in db_ras:
        if isinstance(rec_date.rp_, NoneType):
            p_s=+1 
        elif rec_date.rc_==585:
            mas_ras_585.append(rec_date.ra_)
    for rec_db in db_tpr:
            if isinstance(rec_db.tc_, NoneType):
                p_s=+1
            elif rec_db.tc_ in kody_p and rec_db.ta_ not in mas_pri_595:
                mas1.append(rec_db.ta_ )
            
            elif rec_db.tc_ not in kody_p and rec_db.ta_  in mas_pri:
                mas1.append(rec_db.ta_ )
    for rec_db in db_tra:
            if isinstance(rec_db.vc_, NoneType):
                p_s=+1
            elif rec_db.vc_ in kody_ras and rec_db.va_ not in mas_ras_585:
                mas2.append(rec_db.va_ )
       
            elif rec_db.vc_ not in kody_ras and rec_db.va_  in maszak_ras:
                mas2.append(rec_db.va_)


        
            

levrekv(levpos_p,levpos_ras)
print("Запись данных в файл \n")
vybor_ras(4070001,kura)
vybor_prih(kura,kura_pr)
vybor_ras(4070002,krylo)
vybor_prih(krylo,krylo_pr)
vybor_ras(4070003,okor)
vybor_prih(okor,okor_pr)

for key in kura_pr:
    for item in kura_pr[key]:
        for rec_db in db_tpr:
            if isinstance(rec_db.ta_, NoneType):
                p_s=+1
            elif item==rec_db.ta_ and rec_db.tc_ !=2280303:
                nspisrk.setdefault(key,[])
                nspisrk[key].append(item)

for key in krylo_pr:
    for item in krylo_pr[key]:
        for rec_db in db_tpr:
            if isinstance(rec_db.ta_, NoneType):
                p_s=+1
            elif item==rec_db.ta_ and rec_db.tc_ !=2280305:
                nspisrkr.setdefault(key,[])
                nspisrkr[key].append(item)

for key in okor_pr:
    for item in okor_pr[key]:
        for rec_db in db_tpr:
            if isinstance(rec_db.ta_, NoneType):
                p_s=+1
            elif item==rec_db.ta_ and rec_db.tc_ !=2280304:
                nspisrok.setdefault(key,[])
                nspisrok[key].append(item)




otch.write("Документы на которые стоит обратить внимение \n")
otch.write("\n")
otch.write("Приходные документы с левым поставщиком или с поставщиком 595 и левым товаром: \n")
otch.write(str(set(levpos_p))+"\n")
otch.write("\n")
otch.write("\n")
otch.write("Расходные документы с левым поставщиком или с поставщиком 585 и левым товаром: \n")
otch.write(str(set(levpos_ras))+"\n")
otch.write("\n")
otch.write("Что то не так списано или не тот номеррасхода в приходе прописан\n")
otch.write("Куры: "+str(nspisrk)+"\n")
otch.write("Окорочка: "+str(nspisrok)+"\n")
otch.write("Крыло: "+str(nspisrkr)+"\n")
otch.write("\n")
otch.write("\n")
otch.write("КАРТОЧКИ РАСХОДОВ СЫРЬЯ\n")
otch.write("\n")
otch.write("КУРЫ\n")
for rec in kura:
    for rec_db in db_tra:
        if isinstance(rec_db.va_, NoneType):
            p_s=+1
        elif rec_db.va_ == rec and rec_db.vc_ == 4070001:
            otch.write("Код:4070001____"+"Количество:"+str(rec_db.vi_)+"____"+"Расход № "+str(rec_db.va_)+"\n")
            
            
otch.write("\n")
otch.write("ОКОРОЧКА\n")
for rec in okor:
    for rec_db in db_tra:
        if isinstance(rec_db.va_, NoneType):
            p_s=+1
        elif rec_db.va_ == rec and rec_db.vc_ == 4070003:
            otch.write("Код:4070003____"+"Количество:"+str(rec_db.vi_)+"____"+"Расход № "+str(rec_db.va_)+"\n")
otch.write("\n")
otch.write("КРЫЛЬЯ\n")
for rec in krylo:
    for rec_db in db_tra:
        if isinstance(rec_db.va_, NoneType):
            p_s=+1
        elif rec_db.va_ == rec and rec_db.vc_ == 4070002:
            otch.write("Код:4070002____"+"Количество:"+str(rec_db.vi_)+"____"+"Расход № "+str(rec_db.va_)+"\n")
otch.write("\n")
otch.write("\n")
otch.write("\n")
otch.write("\n")
otch.write("\n")
otch.write("\n")
otch.write("\n")
otch.write("\n")
otch.write("\n")

otch.write("Отчет создан с помощью скрипта на питоне Владом Ш-21. Пользуемся на здоровье)))) \n")
otch.close()
os.startfile('sver_gril.txt')
db_tpr.close()
db_tra.close()
db_pri.close()
db_ras.close()
    
