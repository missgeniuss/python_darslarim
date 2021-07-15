# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 17:32:39 2021

@author: User
"""
def multiple(*numbers):
    """Istalgancha sonlarni qabul qilib, ularning ko'paytmasini 
    qaytaruvchi funksiya"""
    multiples = 1
    for number in numbers:
        multiples *= number
    return multiples
print(multiple(1,2,3,9, 10))
print(multiple())

def student_info(ism, familiya, **info):
    """Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi 
    funkisya yozing. Talabaning ismi va familiyasi majburiy argument, 
    qolgan ma'lumotlar esa ixtiyoriy ko'rinishda istalgancha berilishi 
    mumkin bo'lsin."""
    info['ism'] = ism
    info['familiya'] = familiya
    return info
talaba1 = student_info('Hilola', 'xushmanova', t_yil=2000, baho=5, t_joy='kasan')
talaba2 = student_info('Guli', 'sohibova', t_yil = 1997, fan = 'math')
talabalar = [talaba1, talaba2]
for talaba in talabalar:
    print(talaba)
