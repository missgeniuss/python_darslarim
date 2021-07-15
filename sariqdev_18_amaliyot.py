# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 16:18:13 2021

@author: User
"""

"""Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. Mahsulotlar nomini 
birma-bir qabul qilib, yangi ro'yxatga joylang."""
# mahsulotlar = []
# print("\nBuyurtmani qabul qiluvchi dastur.")
# n = 1
# while True:
#     mahsulot = input(f"{n} - buyurtmangizni kiriting>>>")
#     mahsulotlar.append(mahsulot)
#     ishora = True
#     while True:
#         repeating = input("Yana buyurtma kiritasizmi? (ha/yo'q)>>>")
#         if repeating.lower() == 'ha':
#             n+=1
#             ishora = True #so'zlar to'g'ri kritilayotganini tekshirish uchun o'zgaruvchi
#             break
#         elif not (repeating.lower() == 'ha' or repeating.lower() == 'yo\'q'):
#             print("Faqat ha/yo'q so'zlarini kiritish mumkin! "
#                   "Boshqatdan urinib ko'ring>>>")
#             continue
#         else:
#             ishora = False
#             break
#     if ishora:
#         continue
#     else:
#         break
# # bir xil buyurtmani yo'qotish
# mahsulotlar_set = set(mahsulotlar)       
# print("\nBuyurtmalaringiz ro'yxati: ")
# for mahsulot in mahsulotlar_set:
#     print(mahsulot.title())      

"""e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi 
dastur yozing. Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va 
uning narhi) kiritishni so'rang."""
goods = {} # mollar uchun bo'sh lo'g'at
print("\nBozor mahsulotlarini narxlari bilan choplovchi dastur")
n = 1
while True:
    savol = f"{n} - mahsulotni kiriting>>>"
    name = input(savol)
    price = input(f"{name.title()}ning narxi qancha?>>>")
    goods[name] = price
    sign = True # har safar sikl boshlanmasidan avval ushbu nishonni yana true qiymatga to'g'irlab qo'yish kerak 
    while True:
        repeat = input("Yana mahsulot kiritasizmi? (yes/no)>>>").lower()
        if repeat == 'yes':
            break
        elif not (repeat=='yes' or repeat=='no'):
            print("\nKechirasiz, faqat yes/no so'zlaridan foydalaning!")
            continue
        else:
            sign = False
            break
    if sign:
        n+=1
        continue
    else:
        break

print("\nKiritgan mahsulotlaringiz ro'yxati: ")
for good, price in goods.items():
    print(f"{good.title()} is {price} sum")
    


"""Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi buyurtmasi ro'yxatidagi 
har bir mahsulotni e-bozordagi mahsulotlar bilan solishitiring (tayyor ro'yxat 
ishlatishingiz mumkin). Agar mahsuot e-bozorda mavjud bo'lsa mahuslot narhini 
chiqaring, aks holda "Bizda bu mahsulot yo'q" degan xabarni kor'sating."""
buyurtma = []
i = 1
print("\nBuyurtmani kiritish>>>")
while True:
    mahsulot = input(f"{i} - buyurtmani kiriting>>>")
    buyurtma.append(mahsulot)
    checker = True
    while True:
        takrorlash = input("Yana mahsulot kiritasizmi? (yes/no)").lower()
        if takrorlash == 'no':
            checker = False
            break
        elif not (takrorlash == 'yes' or takrorlash =='no'):
            print("\nIltimos, yes/no so'zlaridan foydalaning! ")
            continue
        else:
            break 
    if checker:
        i+=1
        continue
    else:
        break

# buyurtmani set orqali sartirofka qilish:
buyurtma_set = set(buyurtma)
buyurtma = list(buyurtma_set)
# buyurtma va mahsulotlarni taqqoslash
print("\nBizda mavjud mahsulotlar haqida qisqa hisobot:\n")
for mahsulot in buyurtma:
    if mahsulot not in goods:
        print("{mahsulot.title()} mahsuloti bizda yo'q")
    else:
        print(f"{mahsulot.title()}ning narxi {goods[mahsulot]} so'm")
        
            


