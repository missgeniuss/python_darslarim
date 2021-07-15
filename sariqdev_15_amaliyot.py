# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 08:40:38 2021

@author: User
"""

"""Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. 
Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, alifbo 
ketma-ketligida chiroyli qilib konsolga chiqaring. """
python = {
    'integer':'butun son',
    'float':'haqiqiy son',
    'complex':'kompleks son',
    'imag':'kompleks sonning mavhum qismi',
    'real':'kompleks sonning haqiqiy qismi',
    'set':'to\'plam',
    'list':'ro\'yxat',
    'dictionary':'lo\'g\'at',
    'print':'choplash',
    'upper':'katta harfga o\'girish',
    'title':'bosh harfli qilib chiqarish'
    }
# del python['imag'] # bitta elementni kalit bo'yicha o'chirish
# # bunda .items() metodisiz choplab bo'maydi, chunki u bizga kerakli ikkita qiymatni qaytaradi
# for key, value in sorted(python.items()):
#     print(f"{key.title()} - {value.capitalize()}\n")
    
"""Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi 
davlatlarni, keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida 
konsolga chiqaring. """
davlatlar = {
    'uzbekistan':'tashkent',
    'russia':'moskva',
    'usa':'vashington',
    'indonesia':'jakarta',
    'india':'dehli',
    'ispania':'madrid',
    'frans':'paris',
    'german':'berlin',
    'iran':'tehran',
    }
#aytilgandek choplash, .values, .keys orqali
# print("\nDunyo davlatlari:\n")
# for d in davlatlar.keys(): # yoki "davlatlar:" ni o'zi
#     if d == 'usa':
#         print(f"{d.upper()}\n")
#     else: 
#         print(f"{d.title()}\n")
# print("\nDavlatlarning poytaxtlari:\n")
# for p in davlatlar.values():
#     print(f"{p.title()}\n")
# MENI USULIM
# print("\nDunyo davlatlari va ularning poytaxtlari:\n")
# for d, p in sorted(davlatlar.items()):
#     if d == 'usa':
#         d = d.upper()
#         p = p.title()
#     else:
#         d = d.title()
#         p = p.title()
#     print(f"{d} - {p}")

"""Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning 
poytaxtini konsolga chiqaring. Agar foydalanuvchi lug'atda yo'q davlatni 
kiritsa, "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring."""

# davlat = input("Istalgan davlatni kiriting:>>>")
# capital = davlatlar.get(davlat)
# if davlat in davlatlar.keys(): # yoki davtlatlar ni o'ziyam ishlaydi
#     print(f"{capital.title()}")
# else:
#     print("Bunday davlat yo'q")
#namunadagidek
# if capital == None:
#     print("Kechirasiz, bunday davtlat haqida ma'lumot yo'q")
# else:
#     print(f"{davlat.title()}ning poytaxti {capital.title()}\n")

"""Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini 
kiriting). Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang. 
Foydalanuvchi kiritgan taomlarni menu bilan solishtiring, agar taom menuda 
bo'lsa narhini ko'rsating, aks holda "bizda bunday taom yo'q" degan xabarni 
chiqaring."""
menu = {
        'osh':10000,
        'manti':2000,
        'lag\'mon':13000,
        'norin':45000,
        'sho\'rva':30000,
        'chuchvara':25000,
        'dimlama':50000,
        'kabob':60000,
        'gril':30000,
        'somsa':3000,
        'g\'ilak':23000,
        'blinchik':4000
        }
zakas = []
son = int(input("Nechta taom buyurtma qilasiz?>>>"))
for n in range(son):
    zakas.append(input(f"{n+1} - taomni kiriting:>>>"))
# for z in zakas:
#     if z in menu: #yoki menu.keys():
#         print(f"{z.title()} {menu[z]} so'm")
#     else:
#         print(f"Kechirasiz bizda {z.lower()} yo'q")
# bor yo'q taomlarni alohida choplash
hisob = 0
for z in zakas:
    if z in menu.keys():
        print(f"{z.title()}ning narxi {menu[z]} so'm.\n")
        hisob = hisob + menu[z]
    else:
        print(f"Kechirasiz bizda {z.lower()} yo'q\n")
print(f"Jami so'mma {hisob} so'mga teng")








