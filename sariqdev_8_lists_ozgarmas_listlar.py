# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 20:14:51 2021

@author: User
"""

cars = ['bmw', 'mersedes bens', 'volvo', 'general motors', 'tesla', 'audi']
#ro'yxatni alifbo ketma-ketligida sortlash
#cars.sort()
#print(cars)

#KATTA VA KICHIK HARFLAR
#katta harflar kichik harflardan oldinga keladi, sortlashdan avval bir xil harflarga
# ya'ni katta yoki kichik harflarga o'tkazishimiz kk bo'ladi: 
#lower(), upper(), title(), capitalize() kabilar bilan

#TESKARI TARTIBLASH
#sort(reverse=True) kabi metod bilan ishlaydi
#cars = ['bmv', 'mersedes bens', 'volvo', 'general motors', 'tesla', 'audi']
#cars.sort(reverse=True)
#print(cars)

#SORTED(list) funksiyasi
#asl ro'yxat o'zgarmagan holda sortlab ekranga chiqarish
mehmonlar = ['Odil', 'Shahboz', 'Jo\'rabek', 'Elmira', 'Fayyoza', 'Gulsum', 'Gulmera',\
             'Gulchehra']
print("sorted() bilan ishlangan ro'yxat:", sorted(mehmonlar), "\n")
print("Asl ro'yxat o'zgarmas qoldi:", mehmonlar, "\n")
print("sorted(list, reverse=True) yordamida choplash:", sorted(mehmonlar, reverse=True), "\n")

#SONLAR RO'YXATI
sonlar=[12, 45, -9, 0, 2, -4, 21.3, 3.14]


#RO'YXATNI ORTIDAN BOSHLAB CHIQARISH
# . reverse() metodi orqali ro'yxatni teskari choplash mumkin
fruits = ['peach', 'apple', 'banana', 'apricot', 'grapes']
fruits.reverse()
print(fruits)

#RO'YXAT UZUNLIGI
#len(list) funksiyasi yordamida
uzunlik = len(sonlar)
print("len() funksiyasi integer tipli qiymat qaytaradi:", type(uzunlik))
print("fruits ro'yxatidagi elementlar soni:", len(fruits), "ga teng")

#RANGE
#range(chegara_boshi, chegara_ohiri) bunda boshi kiradi, ohirgi chegara kirmaydi
b = range(100)==range(0,100)
print(b)

#RANGE VA QADAM
#range(1-chegara, 2-chegara, qadam), agar ohirgi qadam berilmasa 0 dan boshlab qabul qiladi
t_sonlar = list(range(0, 99, 11)) # 99 o'zi kirmaydi, qadam = 11
# list() funksiyasi esa range() funksiyadan chiqqan qiymatni o'zlashtiradi
print("99 gacha 11 ga bo'linadigan sonlar:", t_sonlar)
toq_sonlar = list(range(1, 100, 2))
juft_sonlar = list(range(2, 100, 2))
print("1 dan 100 gacha toq (", toq_sonlar, ") va juft sonlar (", juft_sonlar, ") ro'yxati:")


#MIN(), MAX(), SUM()
narxlar = [1245, 34900, 4500, 2300, 39750, 40000]
qimmat = max(narxlar)
arzon = min(narxlar)
jami = sum(narxlar)
print("Eng arzon narx:", str(arzon) + ". Eng qimmat narx", str(qimmat) +\
". Jami:", jami)

#RO'YXATNI KESISH - SLICING
#indekslar yordamida bunda ohirgi chegara kirmaydi
boys = ['Ahad', 'Islom', 'Davron', 'G\'olib', 'Sanjar', 'Shohzamon', 'Bekzod',\
        'Shoxrux', 'Akmal']
boys1 = boys[:-3] # qism ro'yxatni ajratib olish, bunda boshidan -3 chi elementgacha oladi
print("Ro'yxatdan boshidan ohirgi elementni qo'shmasdan choplash:", boys[:-1])
print(cars[:4]) # Ro'yxat boshidan 4-gacha kesadi (0,1,2,3)
print(cars[2:]) # 2-elementdan boshlab ro'yxat oxirigacha kesib oladi

#RO'YXATDAN NUSXA OLISH
#cars = ['bmv', 'mersedes bens', 'volvo', 'general motors', 'tesla', 'audi']
my_cars = cars # ushbu ifoda shunchaki 2 ta nomni ham bitta listga bog'lab qo'yadi
# ya'ni nusxa olmaydi, buni isbotlash ushun bir necha amallar bajaramiz
my_cars.remove('bmw')
my_cars.sort(reverse=True)
print("my_cars ro'yxati:", my_cars)
print("cars ro'yxati:", cars) # bunda ikkala ro'yxat bir xil o'zgarganini ko'ramiz
# demak bu usul nusxa olmaydi. Endi esa nusxa olishni ko'ramiz
real_my_cars = cars[:] # ushbu ifoda yangi ro'yxat yaratadi, nusxa oladi
real_my_cars.append('bmw')
real_my_cars.insert(0, 'rols roys')
print("Avvalgi ro'yxat:", cars)
print("Yangi nusxa olingan ro'yxat:", real_my_cars)
# demak, ushbu nusxa olish ekani isbotlandi

#TUPLE - o'zgarmas ro'yxatdir
# tuple(list) va list(tuple) funksiyalari yordamida bir-biriga o'girish mumkin
toys = ('bus', 'car', 'bear', 'dino', 'snake', 'lizard')
# tupleda indeks bilan murojaat qilish mumkin, lekin o'zgartirish mumkin emas
print(toys[3:]) # bunda 3-elementdan boshlab ohirigacha chiqaradi
toys = list(toys) #ushbu ifoda listga o'zgartiradi toys tuple ni
print("Listga aylangan tuple:", toys)
toys.append("teddy") # endi esa listga qo'llanish mumkin bo'lgan barcha metod 
#va funksiyalar qo'llanilishi mumkin
print("Element qo'shilgan ro'yxat:", toys)
toys = tuple(toys) #kerakli o'zgartirishlardan so'ng yana tuple ga o'tkazib olamiz
print("O'zgartirilgan tuple:", toys)


