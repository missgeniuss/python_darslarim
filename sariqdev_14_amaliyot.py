# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 00:09:24 2021

@author: User
"""

"""otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu 
inson haqida kamida 3 ta m'alumot kiriting (ismi, tu'gilgan yili, shahri, 
manzili va hokazo). Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring 
:Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan"""
# otam = {'ism':'hasan', 't_yil': 1979, 'birthplace':'Kogon'}
# onam = {'ism':'zilola', 't_yil':1981, 'birthplace':'Jizzax'}
# akam = {'ism':'jamshid', 't_yil':1999, 'birthplace':'Qorako\'l'}
# ukam = {'ism':'suxrob', 't_yil':2003, 'birthplace':'buxoro'}
# print(f"Otam {otam['ism'].title()} {otam['t_yil']} - yil {otam['birthplace'].title()}da tug'ilgan.")
# print(f"Onam {onam['ism'].title()} {onam['t_yil']} - yil {onam['birthplace'].title()}da tug'ilgan.")
# print(f"Akam {akam['ism'].title()} {akam['t_yil']} - yil {akam['birthplace'].title()}da tug'ilgan.")
# print(f"Ukam {ukam['ism'].title()} {ukam['t_yil']} - yil {ukam['birthplace'].title()}da tug'ilgan.")

"""Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 
5 ta ism-taom jufltigi bo'lsin. Kamida uch kishining sevimli taomini konsolga 
chiqaring: Alining sevimli taomi osh"""
# taomlar = {
#     'ali':'osh',
#     'ayam':'dimlama',
#     'dadam':'manti',
#     'akam':'makaron palov',
#     'yulduz':'lag\'mon',
#     'muborak':'mastava'
#     }
# print(f"Alining sevimli taomi {taomlar['ali']}")
# print(f"Ayamning sevimli taomi {taomlar['ayam']}")
# print(f"Dadamning sevimli taomi {taomlar['dadam']}")

"""Python izohli lug'ati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z 
(atamani) kiriting (masalan integer, float, string, if, else va hokazo) va har 
birining qisqacha tarjimasini yozing."""
python = {
    'integer':'butun qiymat',
    'float':'o\'nli kasr son',
    'string':'matnli qiymat',
    'if':'agar shart operatori',
    'else':'aks holda',
    'elef': 'aks holda agar',
    'key':'kalit',
    'tuple':'o\'zgarmas ro\'yxat',
    'list':'o\'garuvchan ro\'yxat',
    'dictionary':'lo\'g\'at',
    'error':'xato',
    'set':'to\'plam'
    }
#python['integer']='butun son'

"""Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini 
yuqoridagi lug'atdan chiqarib bering. Agar so'z lu'gatda mavjud bo'lmasa, 
"Bunda so'z mavjud emas" degan xabarni chiqaring.
"""
# javob = python.get(input("Izlayotgan so'zingizni kiriting:>>> "), \
#                    "Bunday qiymat mavjud emas.")
# print(javob)

"""Yuqoridagi vazifani if-else yordamida qiling va natijani ham foydalanuvchiga 
tushunarli ko'rinishda chiqaring."""
# soz = input("Izlayotgan so'zningizni kiriting:>>> ")
# if soz in python.keys():
#     print(f"{soz.title()} so'zi {python[soz]} deb tarjima qilinadi")

#2-usul if yordamida choplash
kalit = input("Istagan so'zingizni kiriting>>> ").lower() #ushbu ifoda kiritlgan
#kalitni kichik harflar bilan o'zlashtiradi
javob = python.get(kalit) #agar mavjud bo'lmasa None qiymat oladi avtomatik tarzda

# if javob == None:
#     print("Bunday so'z mavjud emas")
# else:
#     print(f"{kalit.title()} so'zi {javob} deb tarjima qilinadi.")

if javob: # bu ham yuqoridagi shartga ekvivalent hisoblanadi
    print(f"{kalit.title()} so'zi {javob} deb tarjima qilinadi.")
else:
    print("Bunday so'z mavjud emas")




