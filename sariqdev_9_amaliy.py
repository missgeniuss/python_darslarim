# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 04:25:08 2021

@author: User
"""

ismlar = ["Elmira", "Marjona", "Madina", "Hulkar", "Durdona"]
for ism in ismlar:
    print(f"{ism}, albatta to'yga kelasiz a?")

print(f"Kod {len(ismlar)} marta takrorlandi.")

toq_sonlar = list(range(11, 100, 2))
for son in toq_sonlar:
    print(f"{son} ning kubi {son**3} ga teng\n")
    
# kublar = []
# for son in toq_sonlar:
#     kublar.append(pow(son, 3))
# for s in kublar:
#     print(f"{s}\n")


kinolar = []
for kino in range(5):
    kinolar.append(input(f"{kino + 1} - sevimli kinoyingiz:\n"))
print(f"sevimli kinolarim ro'yxati:\n{kinolar}")


"""Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang,
 va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. 
 Ro'yxatni konsolga chiqaring."""

odamlar_soni = int(input("Bugun necha kishi bilan suhbatlashdingiz?\n>>>"))
odamlar = []
for n in range(odamlar_soni):
    odamlar.append(input(f"Bugun uchratgan {n + 1} - odamingiz?\n"))

print(f"Bugun men {odamlar}lar bilan suhbatlashdim")

# for n in range(5):
#     ismlar[n]=ismlar[n].lower()
# print(ismlar)
# ['elmira', 'marjona', 'madina', 'hulkar', 'durdona']