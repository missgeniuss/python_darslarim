# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 08:23:57 2021

@author: User
"""

cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car == 'gm':
        print(car.upper())
    else:
        print(car.title())
#Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring. 
# for car in cars:
#     if car != 'gm':
#         print(car.title())
#     else:
#         print(car.upper())


#admin user
ism = input("Foydalanuvchi nomingiz, loginni kiriting:\n>>>")
#ism = ism.lower()
if ism.lower() == 'admin':
    print(f"Xush kelibsiz, {ism.title()}. Foydalanuvchilar ro'yxatini ko'rasizmi?\n")
else:
    print(f"Xush kelibsiz, {ism}!\n")
    

# first = int(input("Birinchi sonni kiriting:\n>>>"))
# second = int(input("Ikkinchi sonni kiriting:\n>>>"))
# if first == second:
#     print(f"sonlar teng")


# son = float(input("Istalgan sonni kiriting: "))
# # if son>0:
# #     print(f"{son} musbat son")
# # else:
# #     print(f"{son} manfiy son")
# print("Son manfiy") if son<0 else print("son musbat")

son = float(input("son kiriting: "))
print(son**(1/2)) if son>0 else print("")