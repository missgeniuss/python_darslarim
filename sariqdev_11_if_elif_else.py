# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 08:51:35 2021

@author: User
"""

#11- dars if-elif-else
#Bunday if bilan boshlangan ketma-ketlik bir nechta elif lardan iborat bo'lishi mumkin. 
# son = -50
# if son < 0:
#     print("manfiy son")
# else:
#     print("musbat son")
    
#hayvonot bog'i chiptasi
# yosh = int(input("Yoshingizni kiriting: "))
# if yosh<=4:
#     print("sizga chipta bepul")
# elif yosh<=12:
#     print("sizga kirish 5000 so\'m.\n")
# elif yosh<=18:
#     print("sizga kirish 8000 so'm")
# else: 
#     print("sizga kirish 10000 so'm.")

#QAYTA QAYTA PRINT() NI YOZISHDAN QOCHISH MUMKIN
# yosh = int(input("Yoshingizni kiriting: "))
# if yosh<=4:
#     narx = 0
# elif yosh<=12:
#     narx = 5000
# elif yosh<=18:
#     narx = 8000
# else: 
#     narx = 100000
# print(f"sizga kirish {narx} so'm")

#AND, OR OPERATORS - bir nechta shartlarni jamlash
#Faqat OR
# kun = input("bugun qaysi kun?\n>>>")
# if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#     print("Bugun dam olish kuni")
# else:
#     print("bugun ish kuni")
#faqat AND 
# harorat = float(input("Havo harorati qanday?\n>>>"))
# if kun.lower() =='yakshanba' and harorat>=30:
#     print("Cho'milgani ketdik!")
# else:
#     print("uyda dam olamiz(((yaks")
    
#AND va OR kombinatsiyasi:
# if (kun.lower() == 'yakshanba' or kun.lower() == 'shanba') and harorat >= 30:
#     print("cho'milgani ketdik!")
# elif(kun.lower() == 'yakshanba' or kun.lower() == 'shanba') and harorat < 30:
#     print("uyda dam olamiz...")
    
#restoran dastur BOOL uchun

# narx = 15000
# choy = True #choy oldi
# salat = False # salat olmadi 

# buning kamchiligi qaysi shart bajarilsa, boshqalarini tekshirib o'tirmaydi
"""if-elif-else zanjirida ham else qismi majburiy emas:"""
# if choy and salat:
#     narx = narx + 10000
# elif choy or salat:
#     narx = narx + 5000

# print(f"Jami {narx} so'm")

# narx = 15000
# choy = True # True = 1 
# salat = False # salat false = 0
# non = True # True = 1
# kompot = True 
# assorti = False 
# # bunda True va False o'rniga 1 va 0 ham qo'yishimiz mumkin bo'ladi
# # bu yerda har bir shart mustaqil, har biri tekshiriladi
# if choy: #agar choy olsa
#     print("Mijoz choy ham oldi")
#     narx = narx + 3000

# if salat: #agar salat olsa
#     print("Mijoz salat oldi")
#     narx = narx + 5000

# if non: # agar non olsa
#     print("mijoz non oldi")
#     narx = narx + 2000

# if kompot: # agar kompot olsa
#     print("Mijoz kompot sotib oldi")
#     narx = narx + 5000

# if assorti: # agar assorti olsa
#     print("Mijoz assorti sotib oldi")
#     narx = narx + 15000

# print(f"Jami {narx} so'm bo'ldi.")
    
# ELEMENTNI RO'YXATDA BOR/YO'QLIGINI TEKSHIRISH
# IN va NOT IN
# menu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
# ovqat = input("Nima ovqat buyurasiz?:")
# if ovqat.lower() in menu:
#     print("Buyrutma qabul qilindi!")
# else:
#     print("Afsuski bizda bunday ovqat yo'q.")
#Not in 
"""not operatorini boshqa shartlarning oldidan ham qo'yishimiz mumkin. 
Misol uchun: if not a==5 ifodasi if a!=5 ifodasi bilan bir hil natija qaytaradi."""
# if ovqat.lower() not in menu:
#     print("uzr bizda bu ovqat yo'q")
# else:
#     print("Buyurtma qabul qilindi.")

# RO'YXAT QIYMATLARINI SOLISHTIRISH
menu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
buyurtmalar = ['osh', 'somsa', 'manti', 'shashlik']
if buyurtmalar: #if royxat_nomi: ifodasi agar ro'yxatda bir dona element bo'lsa
# ham TRUE qiymat qaytaradi, aks holda FALSE qiymatini qaytaradi.
    for taom in buyurtmalar:
        if taom in menu:
            print(f"Menuda {taom} bor.\n")
        else:
            print(f"Kechirasiz, menuda {taom} yo'q.\n")

#buyurtmalar bo'sh emasligini tekshirish
# if buyurtmalar:
#     print(f"Ro'yxatda {len(buyurtmalar)} ta taom bor")
# else:
#     print("Ro'yxat bo'sh")




























