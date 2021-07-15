# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 17:56:35 2021

@author: User
"""

# 23- dars: MODULLAR
"""Modul yaratish uchun asosiy dasturimizdagi funksiyalarni yangi 
faylga ko'chiramiz xolos. Modulga oson murojat qilishimiz uchun, 
faylimiz asosiy dasturimiz bilan bitta papkada bo'lgani afzal. 
Bunda adashib ketmaslik uchun, loyihangizning (dasturning) asosiy 
faylini main.py deb nomlash o'rinli. 
    import modul_nomi komandasi bir martta, dastur boshida yoziladi."""

# MODULNI ODDIY CHAQIRIB OLISH USULI
# import avto_info_mod 
# avto1 = avto_info_mod.avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
# avto_info_mod.info_print(avto1)

# QISQA NOM BERISH USULI
# import avto_info_mod as aim 
# avto1 = aim.avto_info("GM", "malibu", 'qora', 'avto', 2020, 43000)
# aim.info_print(avto1)

# # MODUL ICHIDAN ZARUR FUNKSIYALARNI IMPORT QILISH
# from avto_info_mod import avto_info, info_print
"""Bu usulning qulayligi, endi funksiyalarga to'g'ridan-to'g'ri 
murojat qilish mumkin (modul ismini yozmagan holda)"""
# avto2 = avto_info("GM", "malibu", 'qora', 'avto', 2020, 43000)
# info_print(avto2) # endi funksiyani o'zini bemalol ishlatish mumkin

# # FUNKSIYALARGA QISQA NOM BERISH
"""ularning nomi uzunlik qilganda, yoki nomi bir xil funksiyalar uchrab qolganda"""
# from avto_info_mod import avto_info as ainfo, info_print as iprint

# avto2 = ainfo("GM", "malibu", 'qora', 'avto', 2020, 43000)
# iprint(avto2)

# MODUL ICHIDAGI BARCHA FUNKSIYALARNI KO'CHIRIB OLISH
""" ushbu usul modulingiz kichkina bo'lsa ishlatish kk, 
    katta modullarda xatolik beradi.Diqqat! Bir necha sabablarga
    ko'ra bu usuldan foydalanish tavsiya qilinmaydi. Katta 
    modullarda yuzlab funksiyalar bo'lishi mumkin, va funksiya 
    nomi sizning dasturingizdagi boshqa funksiya yoki o'zgaruvchi 
    bilan bir hil nomga ega bo'lsa, dastur xato ishlashiga olib 
    keladi."""
# from avto_info_mod import * # hamma funksiyalarni chaqiradi

# avto1 = avto_info("GM", "malibu", 'qora', 'avto', 2020, 43000)
# info_print(avto1)

# # QONUNIY USUL
# import avto_info_mod
# avto1 = avto_info_mod.avto_info("GM", "malibu", 'qora', 'avto', 2020, 43000)
# avto_info_mod.info_print(avto1)

"""Modullarning ichida nafaqat funksiyalar, balki turli 
o'zgaruvchilarni ham saqlash mumkin. Modul ichidagi o'zgaruvchilarga 
ham huddi yuqoridagi usullar bilan murojat qilish mumkin."""
# from math import pi
# print(pi)
# math ichidagi ayrim funksiyalar
import math
# x = -3.6
# print(math.ceil(x)) # x dan katta yoki teng bo'lgan eng kichik butun sonni qaytaradi
# print(math.fabs(x)) # x ning absolyut qiymatini qaytaradi
# print(math.floor(x)) # x dan kichik yoki teng bo'lgan eng yaqin butun sonni qaytaradi
# print(math.exp(x)) # x^e ni qaytaruvchi funksiya
# print(math.cos(x)) # cos(x) ni qaytaradi
# print(math.sin(x)) # sin(x) ni qaytaradi
# print(math.tan(x)) # tan(x) ni qaytaruvchi funksiya
# print(math.degrees(1)) # x burchakning radian qiymatini darajaga konvertasiya qilish
# print(math.radians(360)) # x burchakning daraja qiymatini radianga konvertasiya qilish 
# print(math.e) # Matematik konstanta  (2.71828...)
# print(math.tau)

# x=400
# print(math.sqrt(x))
# print(math.pow(5, 3))
# print(math.pi)
# log2(x) va log10(x) - x ning 2 va 10-lik logorifmini qaytaruvchi funksiyalar
# print(math.log2(9))
# print(math.log10(100))
# print(math.log(3, 9))
# #  log (a, b), b - asos, a - qiymat


# RANDOM moduli
import random as r
# r dan boshqa joyda foydalanib bo'lmaydi
# # randint()
"""randint(a,b) Bu funksiya a va b oraligi'da tasodifiy butun son qaytaradi."""
# son = r.randint(0,100) # butun son qaytaradi, random son
# print(son)

# # choice()
"""choice(x) x ning ichidan tasodifiy qiymatni qaytaruvchi funksiya. 
Bunda x bir necha elementdan iborat o'zgaruvchi (matn, ro'yxat) 
bo'lishi kerak."""
# ismlar = ['ali', 'vali', 'husan', 'guli', 'hasan'] # ismlar katta o'lchamli bo'lishi maqul
# ism = r.choice(ismlar)
# print(ism)
# # ism = r.choice([]) # bo'sh ro'yxat uzatsak xato qiymat qaytaradi, 
# # 1 tadan ko'p o'lchamli bo'lishi kk
# print(ism)
# print(r.choice(ism))

# x = list(range(0, 51, 5))
# print(x)
# print(r.choice(x))

"""shuffle(x) x ichidagi elementlarni tasodifiy tartibda qaytaruvchi 
funksiya. Bunda x bir necha elementdan iborat o'zgaruvchi (matn, 
ro'yxat) bo'lishi kerak."""
ismlar = ['ali', 'vali', 'husan', 'hasan', 'guli']
print(ismlar)
r.shuffle(ismlar)
print(ismlar)
ism = r.choice(ismlar)
print(ism)
# r.shuffle(ism) # str mn meas ekan
xabar = "BUnda matnli xabar mumkin emas ekan"
print(r.shuffle(xabar))

# x = list(range(11))
# print(x)
# print(r.shuffle(x)) # ushbu qism None qiymat chiqaradi,
# print(x)





