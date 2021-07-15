# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 22:22:32 2021

@author: User
"""

"""Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang. 
Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating"""

# WHILE() 

# O'ZIMNI KODIM)))
# savol = "Yaxshi ko'rgan kitobingizni kiriting. (Dasturni 'stop' so'zi to'xtatadi.>>>"
# kitoblar = []
# kitob = ''
# while kitob != 'stop':
#     kitob = input(savol)
#     if kitob != 'stop':
#         kitoblar.append(kitob)

# if kitoblar:
#     print(f"\nSiz kiritgan kitoblar: ")
#     for k in kitoblar:
#         print(k.title(), end =', ')
# else:
#     print("\nBirorta kitob kiritmadingiz!")
# #so'ngso'z
# print(f"\nDastur tugadi")

# #MUQOBIL DASTUR
# savol = "Sevgan kitobingizni kiriting"
# savol += "(barcha kitoblarni kiritib bo'lgach 'exit' deb yozing): "

# while True:
#     kitob = input(savol)
#     if kitob == 'exit':
#         break
# print('Rahmat!') # ushbu dastur faqat ma'lumot qabul qilarkan, abadiy sikl, break bn chiqiladi
    
"""Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 
7 dan yoshlarga - 2000 so'm, 7-18 gacha 3000 so'm, 
18-65 gacha 10000 so'm, 65 dan kattalarga bepul. 
Shunday while tsikl yozingki, dastur foydalanuvchi 
yoshini so'rasin va chipta narhini chiqarsin. Foydalanuvchi 
exit yoki quit deb yozganda dastur to'xtasin (ikkita shartni 
ham tekshiring)."""
# # break yordamida:
# savol = "Yoshingiz nechada?"
# savol += "(Dasturdan chiqish uchun 'exit' yoki 'quit' so'zlarini yozing')"
# while True:
#     yosh = input(savol)
#     if yosh != 'exit' and yosh != 'quit':
#         yosh = int(yosh)
#         if yosh<7 or yosh>=65:
#             narx = 0
#         elif yosh == 7:
#             narx = 2000
#         elif yosh>7 and yosh<=18:
#             narx = 3000
#         elif yosh>18 and yosh<65:
#             narx = 10000
#         print(f"Chiptangiz narxi {narx} so'm")
#     else:
#         break

# # ishora (flag) yordamida
# savol = "Yoshingiz nechada? "
# savol += "(Dasturdan chiqish uchun 'exit' yoki 'quit' so'zlarini yozing')"
# savol += ">>>"
# sign = True
# while sign:
#     yosh = input(savol)
#     if yosh != 'exit' and yosh != 'quit':
#         yosh = int(yosh)
#         if yosh<7 or yosh>=65:
#             narx = 0
#         elif yosh == 7:
#             narx = 2000
#         elif yosh>7 and yosh<=18:
#             narx = 3000
#         elif yosh>18 and yosh<65:
#             narx = 10000
#         print(f"Chiptangiz narxi {narx} so'm")
#     else:
#         sign = False

# # shart tekshirish
# savol = "Yoshingiz nechada? "
# savol += "(Dasturdan chiqish uchun 'exit' yoki 'quit' so'zlarini yozing')"
# savol += ">>>"
# qiymat = ''
# while not (qiymat =='quit' or qiymat=='exit'):
#     qiymat = input(savol)
#     if qiymat == 'exit' or qiymat == 'quit':
#         break
#     yosh = int(qiymat)
#     if yosh<7 or yosh>=65:
#         narx = 0
#     elif yosh == 7:
#         narx = 2000
#     elif yosh>7 and yosh<=18:
#         narx = 3000
#     elif yosh>18 and yosh<65:
#         narx = 10000
#     print(f"Chiptangiz narxi {narx} so'm")


"""Yuqoridagi dasturni turli usullarda yozib ko'ring (break, ishora, yoki 
shart tekshirish) Quyidagi dasturda bir nechta mantiqiy xatolar bor. 
Jumladan, xusisiy holatlarda tsikl abadiy qaytarilib qolmoqda. Xatolarni 
to'g'rilay olasizmi?"""

savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol).lower()
    if qiymat=='exit':
        break
    elif float(qiymat)<0:
        print("Manfiy sonning ildizini olib bo'lmaydi.")
        continue
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
