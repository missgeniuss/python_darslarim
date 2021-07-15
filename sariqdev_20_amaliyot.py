# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 21:44:53 2021

@author: User
"""
# def user_info(ism, familiya, t_yil, t_joy, email = '', tel = ''):
#     """Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, 
#     tug'ilgan joyi, email manzili va telefon raqamini qabul 
#     qilib, lug'at ko'rinishida qaytaruvchi funksiya. 
#     Lug'atda foydalanuvchi yoshi ham bo'lsin. Ba'zi 
#     argumentlarni kiritishni ixtiyoriy (masalan, 
#     tel.raqam, el.manzil)"""
#     user = {'ism': ism,
#              'familiya':familiya,
#              't_yil':t_yil,
#              't_joy':t_joy,
#              'yosh':2021 - t_yil,
#              'email':email,
#              'tel':tel}
#     return user
#     # return users
# user1 = user_info('ali', 'valiyev', 2001, 'Bo\'lmas', 'ali@gmail.com')

# """Yuqoridagi funksiyani while yordamida bir necha bor chaqiring, 
# va mijozlar degan ro'yxatni shakllantiring. Ro'yxatdagi mijozlar 
# haqidagi ma'lumotni konsolga chiqaring."""
# customers = []
# while True:
#     ism = input("Foydalanuvchi ismini kiriting:>>>")
#     familiya = input("Foydalanuvchi familiyasini kiriting:>>>")
#     t_yil = int(input("Tug'ilgan yilni kiriting:>>>"))
#     t_joy = input("Tug'ilgan joyni kiriting:>>>")
#     yosh = 2021 - t_yil
#     email = input("Emailni kiriting:>>>")
#     tel = input("Telefon raqamini kiriting:>>>")
#     customers.append(user_info(ism, familiya, t_yil, t_joy, email, tel))
#     while True:
#         sign = True
#         savol = input("Yana ma'lumot kiritasizmi? (y/n)").lower()
#         if savol == 'n':
#             sign = False
#             break
#         elif savol == 'y':
#             break
#         else:
#             print("Iltimos, faqat y/n so'zlaridangina foydalaning.")
#             continue
#     if sign:
#         continue
#     else:
#         break
# print("\nMijozlar haqidagi ma'lumotlar:\n")
# for customer in customers:
#     print(f"Mijoz, {customer['ism'].title()} {customer['familiya'].title()}, "
#           f"{customer['t_yil']} - yil {customer['t_joy'].title()}da "
#           f"tug'ilgan. Yoshi {customer['yosh']} da.\nElektron pochtasi: "
#           f"{customer['email']}.\nTelefon raqami: {customer['tel']}")
    
    
# def katta_son_top(son1, son2, son3):
#     """Uchta son qabul qilib, ulardan eng kattasini 
#     qaytaruvchi funksiya"""
#     katta_son = 0
#     if son1>katta_son:
#         katta_son = son1
#     if son2>katta_son:
#         katta_son = son2
#     if son3>katta_son:
#         katta_son = son3
#     return katta_son

# a=int(input("1-sonni kiriting>>>"))
# b=int(input("2-sonni kiriting>>>"))
# c=int(input("3-sonni kiriting>>>"))
# max_val = katta_son_top(a, b, c)
# print(f"{a}, {b}, {c} sonlarining kattasi {max_val} ga teng")

# def aylana_info(radius):
#     """Foydalanuvchidan aylaning radiusini qabul qilib olib, uning 
#     radiusini, diametrini, perimetri va yuzini lug'at ko'rinishida 
#     qaytaruvchi funksiya"""
#     PI = 3.14159
#     aylana = {'radius':radius,
#               'diametr':2*radius,
#               'perimetr':2*PI*radius,
#               'yuz':PI*radius*radius}
#     return aylana
# print(aylana_info(5))
    
def oraliq_tub_son_top(min, max):
    """Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya 
    (tub sonlar —faqat birga va o'ziga qoldiqsiz bo'linuvchi, 1 dan 
    katta musbat sonlar)"""
    tub_sonlar = []
    oraliq_tub_sonlar = []
    for n in range(2, max):
        tub = True
        j = 2
        while j<=n/2:
            if n%j==0:
                tub = False
                break
            else:
                j+=1
        if tub:
            tub_sonlar.append(n)
            
    # print(f"Boshlang'ich ro'yxat {tub_sonlar} dan {min} dan kichkinalarini "
          # f"o'chirib tashlaymiz", end=': ')
    
    for value in tub_sonlar:
        if min > value:
            tub_sonlar.remove(value)
        else: 
            oraliq_tub_sonlar.append(value)
    return oraliq_tub_sonlar
max_chegara = int(input("Yuqori chegarani kiriting>>>"))
min_chegara = int(input("Quyi chegarani kiriting>>>"))
oraliq_list = oraliq_tub_son_top(min_chegara, max_chegara)
print(f"{min_chegara} va {max_chegara} orasidagi tub sonlar", end=": ")
for i in oraliq_list:
    print(i, end=" ")
            
            
    
        
        

# def fibonacci_top(son):
#     """Foydalanuvchidan son qabul qilib, shu son miqdoricha Fibonachchi 
#     ketma-ketligidagi sonlar ro'yxatni qaytaruvchi funksiya yozing.  
#     Ta’rif: Har bir hadi o’zidan oldingi ikkita hadning yig’indisiga 
#     teng bo’lgan ketma-ketlik Fibonachchi ketma-ketligi deyiladi. 
#     Bunda boshlang’ish had ko’pincha 1 deb olinadi.  
#     1, 1, 2, 3, 5, 8, 13, 21, 34, 55,..."""
#     fibonacci = list(range(son)) # boshlang'ich ro'yxat
#     for n in range(son):
#         if n == 0:
#             fibonacci[n]=1
#         if n == 1:
#             fibonacci[n]=1
#         if n>=2:
#             fibonacci[n] = fibonacci[n-1] + fibonacci[n-2]
#     return fibonacci
# n = int(input("Nechta fibonacci soninin choplamoqchisiz?>>>"))
# fibonacci_list = fibonacci_top(n)
# print(f"Dastlabki {n} ta Fibonacci sonlari: ")
# for i in fibonacci_list:
#     print(i, end = ' ')
        
        
        

