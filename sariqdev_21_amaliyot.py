# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 16:22:37 2021

@author: User
"""
# def katta_harf(nomlar):
#     """Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir 
#     matnning birinchi harfini katta harfga o'zgatiruvchi funksiya"""
#     new_nomlar = []
#     while nomlar:
#         nom = nomlar.pop().title()
#         new_nomlar.append(nom)
#     new_nomlar.reverse()    
#     return new_nomlar

# names = ['ali', 'vali', 'hasan', 'aziz']
# names1= katta_harf(names)
# print(names1)
# names2 = katta_harf(names[:])
# print(names2)


# def katta_harf(nomlar):
#     for i in range(len(nomlar)):
#         nomlar[i] = nomlar[i].title()

# names = ['ali', 'vali', 'hasan', 'aziz']
# names1  = katta_harf(names) # bunda funksiya ro'yxat qaytarmaydi,
# # shunchaki namesni o'zini olib katta harfli qilib qo'yadi
# print(f"Boshlang'ich ro'yxat: {names} va natijaviy: {names1}")
    

"""Yuqoridagi funksiyani asl ro'yxatni o'zgartirmaydigan va yangi 
ro'yxat qaytaradigan qilib o'zgartiring"""
def do_title(names):
    names = names[:]
    for i in range(len(names)):
        names[i]=names[i].title()
    return names

ismlar = ['ali', 'guli', 'oysha', 'vali', 'hasan', 'husan']  
yangi_ismlar = do_title(ismlar)
print(ismlar)
print(yangi_ismlar)      


"""Darsimiz davomida yozgan bahola funksiyasini .pop() metodidan 
foydalanmasdan va asl ro'yxatga o'zgartirish kiritmasdan faqat 
lug'at qaytaradigan qilib yozing"""

def bahola(ismlar):
    # ismlar = ismlar[:] # algoritm ro'yxatga o'zgartirish kiritayotgani yo'q
    # chunki for dan foydalanilgan
    baholar = {}
    for ism in ismlar:
        baho = input(f"{ism.title()}ning bahosi>>>")
        baholar[ism] = int(baho)
    return baholar
talabalar = ['ali', 'guli', 'oysha', 'vali', 'hasan', 'husan'] 
baholanganlar = bahola(talabalar)
print(baholanganlar)
print(talabalar)

        
        