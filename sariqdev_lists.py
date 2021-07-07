# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 13:10:59 2021

@author: NewMoon
muallif: Hilola Xushmanova

"""
mevalar= ['olma', 'shaftoli', 'anjir', 'o\'rik', "olxo'ri"] # matnli ro'yxat
narxlar=[12000, 13000, 15000, 5000, 22000, 3200, -2300] # sonli ro'yxat
sonlar=["bir", 'ikki', 3, 4, 5] #sonlar va matnlar, aralash ro'yxat
ismlar=[] # bo'sh ro'yxat

print("Birinchi meva", mevalar[0].title()) # indeks orqali ro'yxat elementlariga murojaat
print("Ikkinchi meva", mevalar[1].upper()) # shuningdek, element string bo'lgani uchun string metodlarini qo'llash mn
# "+" and "-" indexing
#"-" indeks ohirgi elementni ro'yxat hajmini bilmasdan turib chiqarish mumkin
mantiqiy = mevalar[0] == mevalar[-1]
print(mantiqiy)
#ro'yxat nomiga ko'plik qo'shish kk, tushunish oson bo'lishi uchun

'''elementlarni o'zgartirish'''
narhlar = [12000, 18000, 10900, 22000]
narhlar[0] = 13000 # 1-qiymatni 13000 ga o'zgartiramiz
narhlar[2] = 11000 # 3-qiymatni 11000 ga o'zgartiramiz
narhlar[3] = narhlar[3]+2000 # 4-qiymatga 2000 qo'shamiz
print(narhlar)

cars = ['Nexia', 'Nexia 3', 'Malibu', 'Lasetti', 'Tracker']
car1 = 'Matiz'
cars.append(car1) #append() metodi ro'yxat ohiriga biror element qo'shadi
cars.append('Damas')
print("Ro'yxatga 2 ta mashina qo'shilgan", cars)

'''Ro'yxatdan element o'chirish'''
# buning uchun 2 ta usul mavjud
# del list[index_of_elem] ushbu del operatori shu tarzda indeksdagi elementni o'chiradi
del cars[1]
print("Doing the code cars.del(1):", cars)

#lement qiymati bo'yichi o'chirish uchun esa .remove(qiymat) metodidan foydalanamiz. 
#Buning uchun qavs ichida o'chirib tashlash kerak bo'lgan qiymatni yozamiz
cars.remove('Matiz') # remove() metodi qiymat bo'yicha 1 chi uchragan qiymatni o'chiradi
cars.remove('Malibu') # ya'ni 2 ta bo'lsa faqat 1 chisini
print("Ro'yxat ichidan ikkita qiymat 'Malibu' va 'matiz' o'chirilgan:",cars)

cars.insert(0, 'Malibu') # list.insert(index, value)
cars.insert(-1, 'Tiko') # insert() metodi berilgan index ga berilgan qiymatni qo'yadi
print("Ro'yxat boshi va ohiriga ikkita mashina qo'shilgan:", cars)


hayvonlar = ['it', 'mushuk', 'sigir', 'qo\'y', 'quyon', 'mushuk']

#elementni sug'urib olish
 # list.pop(index_of_element) metodi
bozorlik = ['yog\'', 'un', 'piyoz', 'banan', "go'sht"]
mahsulot = bozorlik.pop(3)
print("Men " + mahsulot + " sotib oldim")
print("Olinmagan mahsulotlar: ", bozorlik)
mahsulot2 = bozorlik.pop() # agar pop() ga index ko'rsatilmasa ohirgi elementni o'ziga oladi
print(mahsulot2)
print(bozorlik)