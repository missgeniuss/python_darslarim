# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 15:26:22 2021

@author: User
"""

# def yil_hisobla(ism, yosh):
#     """Foydalanuvchi ismi va yoshini so'rab, 
#     uning tug'ilgan yilini hisoblaydigan funksiya"""
#     print(f"{ism.title()} {2021-yosh} - yilda tug'ilgan.")

# yil_hisobla('hasan', 28)
# yil_hisobla(ism='husan', yosh=23)

# def daraja_hisobla(son):
#     """Foydalanuvchidan son olib, uning kvadrati va 
#     kubini konsolga chiqaruvchi funksiya"""
#     print(f"{son} ning kvandarti: {son**2}\n"
#           f"{son} ning kubi: {son**3}")
    
# daraja_hisobla(4)

# def juft_toq_tekshir(son):
#     """Foydalanuvchidan son olib, son juft yoki toqligini 
#     konsolga chiqaruvchi funksiya"""
#     if not son%2 == 0:
#         print(f"{son} toq son")
#     else:
#         print(f"{son} juft son")
# # funksiyani tekshirish        
# juft_toq_tekshir(-19) 
   
# def katta_son_top(a, b):
#     """Foydalanuvchidan ikkita son olib, ulardan kattasini 
#     konsolga chiqaruvchi funksiya. Agar sonlar teng bo'lsa 
#     "Sonlar teng" degan xabarni chiqaradi."""
#     if a == b:
#         print("Sonlar teng.")
#     elif a>b:
#         print(f"{a} va {b} sonlarining kattasi: {a}")
#     else:
#         print(f"{a} va {b} sonlarining kattasi: {b}")
# # ishlatib ko'rish
# katta_son_top(23, 100)

# def ydaraja_hisobla(x, y):
#     """Foydalanuvchidan x va y sonlarini olib, 
#     x^y ni konsolga chiqaruvchi funksiya."""
#     print(f"{x} ning {y} - darajasi {x**y} ga teng.")
# # funksiyani ishlatish    
# ydaraja_hisobla(1.5, 2)  

def kvadrat_daraja_hisobla(asos, daraja=2): # standart qiymat 2 ga teng
    """Foydalanuvchidan son olib, funksiyada daraja uchun 
    2 standart qiymatini olgan holda natijani chiqaruvchi funksiya.""" 
    print(f"{asos} ning {daraja} - chi darajasi: {asos**daraja}")

kvadrat_daraja_hisobla(11) 
kvadrat_daraja_hisobla(12,4) 

def buluvchi_top(son):
    """Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha 
    bo'lgan sonlarga qoldiqsiz bo'linishini tekshiruvchi va 
    Natijalarni konsolga chiqaruvchi funksiya."""
    # for n in range(2, 11):
    #     if son % n == 0:
    #         print(f"{son} {n} ga qoldiqsiz bo'linadi.")
    
    #ikkinchi usul
    buluvchi_list = []
    for n in range(2, 11):
        if son%n == 0:
            buluvchi_list.append(n)
    print(f"{son} ning 10 gacha bo'luvchilari ro'yxati: ")
    for buluvchi in buluvchi_list:
        print(buluvchi, end = ' ')

savol = int(input("Sonni kiriting:>>>"))        
buluvchi_top(savol)
    