# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 17:46:16 2021

@author: User
"""

#12-dars: ENG KO'P QILINADIGAN XATOLAR
#Xatolar bilan ishlash

#muallif: Hilola Xushmanova

#1) SYNTAX ERROR -  SINTAKS XATOLAR
# Sintaks xatolik bor dasturni Python bajarmaydi.
# print "Salom" # ishlatganimizda ham xato beradi, ularni kodni yozish oldidan ham chiqariladi
#print("Hello World!")

# print("Hello World" # EOF = End of function funksiya yakunida xato bor
# bunaqa xatolar sinchiklab qo'lda tekshiriladi
# print("Hello World  
#EOL = end of line, qator ohirida xato
#EOL (End of Line - qator yakuni) xatoligi sintaks xatolikning bir turi bo'lib, odatda qator oxirida qo'shtirnoq (birtirnoq) ni yopish esdan chiqqanda yuzaga keladi.
     
#2) INDENTATION ERROR - bo'sh joy xatosi
# print("Hello World!") #unexpected indent 

# print("O'ngacha sanaymiz:")
# for n in range(10):
# print(n+1) #expected an indent block

"""Joy tashlash ya'ni indent standarti qancha? 
1) TAB
2) SPACE*4
bunda joylar bir xil tashlab ketiladi."""
#Aslida, hech bo'lmaganda 1 harflik bo'sh joy qoldirish ham bizni 
#IndentationError dan xalos qiladi. LEKIN, biz dastur davomida bir hil joy tashlashga odatlanishimiz kerak. 

# for n in range(10):
#  print(n)
#     print(n+1)  # unexpected indent

# 3) RUNTIME ERROR - ushbu xatolik dastur bajarilganda chiqariladi, turlari juda ko'p
#TypeError - ma'lum turdagi variable ustida bajarib bo'lmaydigan amal bajarsak
# son = input("Istalgan son kiriting:>>>")
# son = int(son)
# print(f"{son} ning kvadrati {son**2} ga teng") #TypeError, ya'ni str ni kvadratini hisoblolmaydi

#NameError - operator, funksiya, o'zgaruvchi nomini xato yozsak kelib chiqadi
# prit("Hello Wordl!") # name 'prit' is not defined
# mevalar = ['olma', 'behi', 'gilos']
# for meva in mvalar: #name 'mvalar' is not defined
#     print(meva)

#ValueError
# son = float(input("Istalgan son kiriting:>>>"))
# if son>=0:
#     print("musbat son")
# else:
#     print("manfiy son") # ushbu kodga float tipli son kiritsak bunda xato chiqaradi, 
#chunki int() funksiyasi kritilgan qiymatni agar int bo'lsagina o'gira oladi
# to'g'rilash uchun esa float() dan foydalanish kk yoki aynan butun son kiriting deyish kk

#IndexError - noto'g'ri indeks bilan murojaat qilish
# mevalar = ['olma', 'behi', 'gilos']
# print(mevalar[3]) # IndexError: list index out of range
# index ning maksimal qiymati len(list)-1 bo'lishi mumkin

#ZeroDivisionError
# x, y = 50, 50
# z=250/(x-y) #ZeroDivisionError: division by zero

#MANTIQIY XATOLAR - o'zingiz dastur davomida yo'l qo'yadigan xatolar
"""Python mantiqiy xatolarni aniqlamaydi va dastur bajarilaveradi (lekin 
kutilgan natija chiqmaydi). Mantiqiy xatoliklar mutlaqo topilmasdan ham qolib
ketishi, va dastur bozorga chiqqanidan so'ng aniqlanishi tabiiy hol. Shuning 
uchun ham aksar dasturlar tez-tez yangilanib turadi."""
# radius = 5
# pi = 4.14 # bunda pi qiymati xato kiritildi
# aylana_yuzi = pi*radius**2
# print(aylana_yuzi)

#son ildizi uchun masala
# son = float(input("Istalgan son kiriting:>>>"))
# # ildiz = son**1/2 # shu yerda ildiz umumiy qavs () ga olinishi kk edi
# ildiz = son**0.5  #yoki ildiz = son **(1/2)  # muqobil yechimlar
# print(f"{son} ning ildizi {ildiz} ga teng")

#yana bir mantiqiy xato
# mevalar = ['olma', 'behi', 'uzum']
# for meva in mevalar:
#     print(meva)
#     print("Dastur tugadi") # xato bu yerda ushbu qator ham for() sikli ichiga tushib qolgan









