# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 04:52:43 2021

@author: NewMoon
"""

#10-dars tarmoqlanish

#muallif: Hilola Xushmanova

avtolar = ['audi', 'bmw', 'volvo', 'kia', 'hyundai']

# for avto in avtolar:
#     print(avto.title()) # bunda hammasini bosh harf bilan chiqaradi 
#     # lekin bu kod BMW uchun to'liq ishlamaydi

for avto in avtolar:
    if avto == 'bmw': # shart
        print(avto.upper()) #avto ni hamma harflarini katta qilib oladi
    else: # aks holda
        print(avto.title()) # avto ni bosh harf bilan yozadi

# ism = 'Ali'
# ism.lower() == 'ali'

# ism = input("Ismingiz nima?\n>>>")
# if ism.lower() != 'ali':
#     print(f"Uzr,{ism.title()} biz Alini kutyapmiz.")
# else:
#     print("Salom, Ali!")
        
#sonlar bilan ishlash
# javob = float(input("12X6 nechchiga teng?\n>>>"))
# if javob!= 72:
#     print("Javobingiz xato!")
    
#ruxsatni taqiqlash algoritmi:
# yosh = int(input("Yoshingiz nechada?\n>>>"))
# if yosh>=18:
#     print("Xush kelibsiz!")
# else:
#     print("Tizimga kirishga ruxsat yo'q!")
    
#login o'lchami
# login = input("yangi login tanlang:")
# if len(login)<=5:
#     print("login 5 harfdan ko'proq bo'lishi shart")


# t_yil = int(input("Tug'ilgan yilingizni kiriting:"))
# #yosh = 2021 - t_yil
# if 2021 - t_yil<=18:
#     print(f"yoshingiz {2021 - t_yil} da ekan. \nSizga kirish mumkin emas!")
# else:
#     print("Xush kelibsiz!")

# yosh = int(input("Yoshingiz nechada?\n>>>"))
# if yosh > 65: print("Siz Covid-19 risk guruhida ekansiz!")   
x, y = 25, 50
print("x>y") if x>y else print("x<y")



