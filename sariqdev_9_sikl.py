# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 03:59:01 2021

@author: User
"""
mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
for mehmon in mehmonlar:
#     print("Salom,", mehmon)
# print("Xayr,", mehmon) # bunda mehmonning ohirgi qiymatini qabul qilib choplaydi
    print(f"Hurmatli {mehmon}, sizni to'yga taklif etamiz!")
    print("Hurmat bilan Xushmanovlar oilasi")

#sonlar bbilan ishlash
sonlar = list(range(1,11))
for son in sonlar:
    print(f"{son} ning kvadrati {son**2} ga teng.\n")

sonlar1 = list(range(11))
sonlar_kvadrati = []
for son in sonlar1:
    sonlar_kvadrati.append(son**2)

print(sonlar1)
print(sonlar_kvadrati)

dostlar = []
print("5 ta eng yaqin do'stingiz kim? ")
for n in range(5):
    dostlar.append(input(f"{n+1} - do'stingizni kiriting:\n"))
print(dostlar)