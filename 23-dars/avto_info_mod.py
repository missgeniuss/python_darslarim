# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 17:44:52 2021

@author: NewMoon
"""

# 23-dars: MODULLAR

# modullar bu alohida fayl, funksiyalarni yashirish uchun, oson tushunish uchun
# katta dasturlar bir nechta modullardan iborat bo'ladi
# ushbu modul boshqa dasturlarda ham foydalanish mumkin

# def avto_info(kompaniya, model, **info):
#     info['kompaniya'] = kompaniya

def avto_info(kompaniya, model, rang, korobka, yil, narx = None):
    """Avtomobil haqida ma'lumotlar lo'g'atini yaratuvchi dastur"""
    avto = {"kompaniya":kompaniya,
            'model':model,
            'rang':rang,
            'korobka':korobka,
            'yil':yil,
            'narx':narx}
    return avto

def avto_kirit():
    """Avtomobillarni kirituvchi funksiya"""
    print("Saytimizdagi avtomobillar ro'yxatini shakllantiramiz.")
    avtolar =[]
    while True:
        print("\nQuyidafi ma'lumotlarni kiriting>>>")
        kompaniya = input("Ishlab chiqaruvchi: ")
        model = input("Modeli: ")
        rang = input("Rangi: ")
        korobka = input("Korobka: ")
        yil = int(input("Ishlab chiqarilgan yili: "))
        narx = input("Narxi: ")
        # Foydalanuvchi kiritgan ma'lumotlarni avto_info orqali
        # Lo'g'at shakllantirib, har bir lo'g'atni ro'yxatga qo'shamiz
        avtolar.append(avto_info(kompaniya, model, rang, korobka, yil, narx))
        # yana avto qo'shasizmi deb so'raymiz
        javob = input("Yana avto qo'shasizmi? (yes/no)>>>").lower()
        if javob == 'no':
            break
        return avtolar
        
def info_print(avto_info): 
    """Mahsina haqidagi ma'lumotlarni choplovchi funskiya"""
    print("\nSalonimizdagi avtolar:")
    
    print(f"{avto_info['rang'].title()} {avto_info['model'].title()}. Narxi: {avto_info['narx']}.")   