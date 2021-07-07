# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 10:52:48 2021

@author: User
"""

#elef = else if = aks holda agar
#Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son 
#kiritsa "Rahmat!", agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.

# son = int(input("Juft son kiriting: "))
# if son%2==0:
#     print("Raxmat!")
# else:
#     print("Bu juft son emas.")
    
"""Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm"""

# yosh = int(input("Yoshingiz nechada?>>>"))
# if yosh<=4 or yosh>=60:
#     narx = 0
# elif yosh<=18:
#     narx = 10000
# else: 
#     narx = 20000
# print(f"Sizga muzeyga kirish narxi {narx} so'm")

"""Foydalanuvchidan ikkita son kiritishni so'rang, sonlarni solishtiring va 
ularning teng yoki katta/kichikligi haqida xabarni chiqaring"""
# son1 = float(input("1 - sonni kiriting:>>>"))
# son2 = float(input("2 - sonni kiriting:>>>"))

# if son1 != son2:
#     if son1 > son2:
#         print(f"{son1} > {son2} ifoda o'rinli\n")
#     else:
#         print(f"{son2} > {son1} ifoda o'rinli\n")
# else:
#     print("Sonlar teng")

"""mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. 
Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta 
mahsulot kiritishni so'rang. Savatdagi elementlarni, mahsulotlar ro'yxati bilan 
solishtiring va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda, 
"Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring."""

# mahsulotlar = ['non', 'banan', 'yogurt', 'anor', 'apelsin', 'un', 'tuxum', 'qulupnay',
#                'tarvuz', 'qovun', 'qo\'ziqorin', 'karam', 'makaron', 'pishloq']
# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1} - mahsulotni qo'shing:>>>\n"))

# for mahsulot in savat:
#     if mahsulot.lower() in mahsulotlar:
#         print(f"Do'konimizda {mahsulot.title()} bor.\n")
#     else:
#         print(f"Do'konimizda {mahsulot.title()  } yo'q\n")
        
"""Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot
kiritishni so'rang. Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yang, 
bor_mahsulotlar degan ro'yxatga, do'konda yo'q mahsulotlarni esa mavjud_emas
degan ro'yxatga qo'shing.  Agar mavjud_emas ro'yxati bo'sh bo'lsa, 
"Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni, aks holda esa
"Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring."""

# mahsulotlar = ['non', 'banan', 'yogurt', 'anor', 'apelsin', 'un', 'tuxum', 'qulupnay',
#                'tarvuz', 'qovun', 'qo\'ziqorin', 'karam', 'makaron', 'pishloq']    

# savat = []
# for n in range(5):
#     savat.append(input(f"{n+1} - mahsulotni kiriting:>>>"))

# bor_mahsulotlar = []
# yoq_mahsulotlar = []

# for mahsulot in savat:
#     if mahsulot.lower() in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         yoq_mahsulotlar.append(mahsulot)

# if yoq_mahsulotlar: 
#     print(f"Quyidagi mahsulotlar do'konimizda yo'q: \n")
#     for m in yoq_mahsulotlar:
#         print(f"{m.lower()}\n")
# else:
#     print(f"So'ragan barcha mahsulotlaringiz do'konimizda bor.")
    
"""foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. 
Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan 
loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. 
Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" 
aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring."""

# users = ['Akmal', 'newmoon', "UniCorn", 'spyder', 'NEW AGE']
# login = input("Yangi login kiriting: ")

# if login.lower() in users:
#     print(f"Xush kelibsiz, {login}")
# else:
#     print(f"Kechirasiz ushbu {login} band! Boshqa login tanlang" )


"""Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan
 sonni 2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini 
 konsolga chiqaring. """

son = int(input("Biror butun son kiriting:>>>"))

# for n in range(2, 11):
#     if son % n == 0:
#         print(f"{son} soni {n} ga qoldiqsiz bo'linadi")

for n in range(2, 11):
    if not (son%n):
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi.")











