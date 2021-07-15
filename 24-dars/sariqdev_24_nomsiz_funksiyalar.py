# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 22:10:29 2021

@author: User
"""

# 24 - dars: SO'NGSO'Z, NOMSIZ FUNKSIYALAR

# import math

# def nom(argument): # buning hajmi cheklanmagan
#     return ifoda

# LAMBDA - nomsiz funksiyalar
# cheklangan hajmdagi ifoda, lekin argumentlar soni cheklanmagan
# lambda argument1, argument2,...argumentn: ifoda = argument1 +,..,+ argumentn

# uzunlik = lambda pi, r: 2*pi*r # bu yerda uzunlik identifikator
# print(uzunlik(math.pi, 10))
"""Kodni tahlil qilamiz, 1-qatorda math modulini chaqirib oldik. 
2-qatorda lambda funksiyani yaratdik, funksiyamiz pi va r 
argumentlarini qabul qilib, 2*pi*r qiymatni qaytaradi. Funksiyaga 
nom bermadik, lekin unga uzunlik identifikatori orqali murojat 
qilishimiz mumkin. 3-qatorda funksiyamizga murojat qildik va 
natijani konsolga chiqardik."""

# kvadrat = lambda x, y: x**y
# print(kvadrat(3, 2))
"""Gap shundaki, lambda finksiyalarning asl mohiyati boshqa 
funskiyalar bilan birga ishlaganda ko'rinadi. """
# # lambda funksiyani boshqa funksiyalar ichida qo'llash qulay
# def daraja(n):
#     return lambda x: x**n # ushbu funksiya funksiya yasaydigan funksiyadir
"""Quyidagi dasturda biz avval daraja degan funksiya yasadik, bu 
funskiyamiz n degan o'zgaruvchi qabul qilib oladi va funksiya 
ichidagi noma'lum x ning n-darajasini qaytaradi. Aslida daraja bu 
funksiya yasaydigan funksya bo'ldi. Xo'sh, undan qanday foydalanamiz?
4-5-qatorlarda esa daraja funksiyasidan yana 2 ta funksiya yasadik: 
kvadrat - kiritilgan sonning kvadratini hisoblaydi, kub - kiritilgan 
sonning kubini hisoblaydi."""
# kub = daraja(3) # kub degan funksiya yaratdik 
# print(kub(4)) # 4 ning kubini choplaydi
# kvadrat = daraja(2) # kvadrat degan funksiya yaratdik
# print(kvadrat(5)) # 5 ning kvadratini choplaydi
# son = int(input("Sonni kiriting>>>"))
# print(f"{son} ning kvadrati {kvadrat(son)} ga, "
#       f"kubi esa {kub(son)} ga teng.")

# MAP() funskiyasi
"""Bu funksiya argument sifatida ro'yxat (yoki lug'at) va boshqa bir 
funksiyani qabul qilib, ro'yxat elementlariga qabul qilingan funksya 
yordamida ishlov beradi. Tushunarli bo'lish uchun quyidagi misolni 
ko'ramiz."""
# from math import sqrt # sonning kvadrat ildizini hisoblaydigan funksiya

sonlar = list(range(11))
# ildizlar = list(map(sqrt, sonlar)) # ro'yxatdan hammasini ildizini hisoblaydi
# map funksiyasi ro'yxat qabul qilib, obyekt qaytaradi, shuning uchun listga konvert qilib olamiz
# print(ildizlar)

# 1-UZUN USUL
# def daraja2(x):
#     """Berilgan sonni kvadratini qaytaruvchi funksiya"""
#     return x*x
# print(list(map(daraja2, sonlar)))

# 2-QISQA USUL
# kvadratlar = list(map(lambda x:x*x, sonlar))
# print(kvadratlar)
"""Yuqoridagi misolda, endi daraja degan funksiyani yaratib 
o'tirmasdan, to'g'ridan-to'g'ri map() ni ichiga darajani 
hisoblovchi lambda funksiya uzatdik."""

# # 3-SIKLLI UZUN USUL
"""map() funksiyasi bo'lmaganida biz bunday dasturlarni for 
yordamida yozishimiz kerak bo'lar edi:"""
# kvadratlar = []
# for son in sonlar:
#     kvadratlar.append(son*son)
# print(kvadratlar)

# map() funksiyasiga bir nechta ro'yxatlar ham uzatish mumkin:
# a = [4,5,6]
# b = [7,8,9]
# a_plus_b = list(map(lambda x, y: x+y, a,b)) # x ni o'rniga a, y ni o'rniga b
# print(a_plus_b)


# map() istalgan ko'rinishdagi ma'lumot turlari bilan ishlaydi:
ismlar = ['ali', 'vali', 'hasan', 'husan']
print(list(map(lambda matn: matn.upper(), ismlar)))    


# FILTER() funksiyasi
"""Bu funksiya ham argument sifatida ro'yxat va boshqa funskiyani 
qabul qilib oladi va berilgan ro'yxat elementlarini berilgan 
funksiya yordamida saralaydi. Bunda argument sifatida uzatilgan 
funksiya mantiqiy qiymat qaytarishi kerak (True yoki False)."""
import random as r

sonlar = r.sample(range(100), 10) # 0 dan 99 gacha bo'lgan 10 ta tasodifiy son
print(sonlar)

# def juftmi(x):
#     """x juft bo'lsa True, toq bo'lsa false qaytaradi"""
#     return x%2==0

# juft_sonlar = list(filter(juftmi, sonlar)) # filter() funsiyamiz juftmi 
# funksiyasi yordamida juft sonlarni saralab oladi
# print(juft_sonlar)

# agar ushbu juftmi() funksiyasi 1 marta ishlatiladigan kod bo'lsa

juft_sonlar = list(filter(lambda son:son%2==0, sonlar))
print(juft_sonlar)

# LAMBDA YORDAMIDA MATNLAR BILAN ISHLASH
"""Keling endi filter() funksiyasi yordamida matnlarni saralashga 
ham misollar ko'raylik. Quyidagi dastur mevalar ro'yxatidan b 
harfiga boshlanuvchi mevalarni ajratib oladi. Bu yerda biz 
matnlarga tegishli bo'lgan .startswith() metodidan foydalandik. 
Bu metod, berilgan matn shu harfdan boshlanadimi yoki yo'q 
tekshiradi va True yoki False qiymat qaytaradi"""

mevalar = ['behi', 'olma', 'gilos', 'banan', 'olcha', 'shaftoli', 'olxo\'ri']
# harf = 'o'
# mevalar_b = list(filter(lambda meva:meva.startswith(harf), mevalar)) 
# print(mevalar_b)
mevalar2 = list(filter(lambda meva:len(meva)<=5, mevalar))
print(mevalar2)

# 'o' harfi bilan bsohlanib, 'a' harfi bilan tugaydigan so'zlarni lsitga joyladi.
mevalar3 = list(filter(lambda meva: (meva.startswith('o') and meva.endswith('a')), mevalar))
print(mevalar3)






