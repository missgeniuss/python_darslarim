# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 16:17:50 2021

@author: User
"""

"""Uchta son orasidan eng kichigini topadigan dastur tuzing"""
#1-usul

a = int(input("Birinchi sonni kiriting:>>>"))
b = int(input("Ikkinchi sonni kiriting:>>>"))
c = int(input("Uchinchi sonni kiriting:>>>"))
max_val = 0
if (a==b and b==c and a==c):
    print("Hamma sonlar teng")
    max_val = a
else: 
    if (a>b) and (a>c):
        max_val = a
    elif (b>a) and (b>c):
        max_val = b
    elif c>a and c>b:
        max_val = c
    print(f"{a}, {b}, {c} sonlari orasida maksimali {max_val} ga teng")
    
#2-usul

# sonlar = []
# for n in range(3):
#     sonlar.append(int(input(f"{n+1} - elementni kiriting:>>>")))

# max_val = max(sonlar)
# print(f"{sonlar} ro'yxatidagi maksimal qiymat: {max_val}")

#3-usul



