# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 11:57:17 2021

@author: User
"""

"""Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar 
haqidagi ma'lumotlarni lug'at ko'rinishida saqlang. Lug'atlarni bitta 
ro'yxatga joylang, va har bir shaxs haqidagi ma'lumotni konsolga chiqaring."""
# muhammad = {
#     'ism':'muhammad s.a.v',
#     't_yil':570,
#     'place':'arabistonning makka shahri',
#     'd_year':632,
#     'd_place':'madina',
#     'asarlar':['qur\'on']
#     }
# navoiy = {
#     'ism':'alisher navoiy',
#     't_yil':1441,
#     'place':'hirot',
#     'd_year':1501,
#     'd_place':'hirot',
#     'asarlar':['xamsa', 'lisson ut-tayr', 'mahbub ul-qulb']
#     }
# temur = {
#     'ism':'amir temur',
#     't_yil':1336,
#     'place':'kesh',
#     'd_year':1405,
#     'd_place':'o\'tror',
#     'asarlar':['temur tuzuklari', 'temurnoma']
#     }
# bobur = {
#     'ism':'bobur mirzo',
#     't_yil':1483,
#     'place':'fergana',
#     'd_year':1530,
#     'd_place':'kabul',
#     'asarlar':['boburnoma', 'humoyunnoma', 'mubayyin', 'xatti boburiy', 'volidiya']
#     }
# persons = [muhammad, navoiy, temur, bobur]
# for person in persons:
#     # yosh = person['d_year'] - person['t_yil']
#     print(f"{person['ism'].title()} {person['t_yil']} - yilda",
#           person['place'].title() + "da tavvalud topgan. "
#           f"{person['d_year']} - yil {person['d_place']}da "
#           f"{person['d_year'] - person['t_yil']} yoshida vafot etgan.")
    
# """Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham 
# qo'shing. For tsikli yordamida muallifning ismi va uning asarlarini konsolga 
# chiqaring."""  
# for person in persons:
#     print(f"\n{person['ism'].title()} ning mashhur asarlari: ", end = '')
#     for asar in person['asarlar']:
#         print(f"{asar.title()}", end=', ')
#     print(end='.')

"""Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida 
so'rang. Do'stingiz ismi kalit, uning sevimli kinolarini esa ro'yxat 
ko'rinishida lug'artga saqlang.  Natijani konsolga chiqaring."""
# dostlar = {
#     'ali':['shaytanat', 'oq kema', 'alvon yelkanlar'],
#     'vali':['bryus li', 'leytenant', '18-kvadrat', 'ilhaq'],
#     'maryam':['shamollarda qolgan hislarim', 'uch savdoyi', 'devdas', 'sen yetim emassan',
#               'daydi qizning daftari', 'oyijon', 'vatan'],
#     'unsun':['qodirxon', 'armon', 'senga oshiqman', 'chegara ortida', 'gumbaz ostida']
#     }
# for key, value in dostlar.items():
#     print(f"\n{key.title()}ning sevimli kino-seriallari: ", end = '')
#     for kino in value:
#         print(f"{kino.title()}, ", end = '')
#     # print(end = '.')

"""Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar haqida 
ma'lumotlarni lug'at ko'rinishida saqlang. Har bir davlat haqida ma'lumotni 
konsolga chiqaring."""
davlatlar = {
    'o\'zbekiston':{'poytaxt':'toshkent',
                  'hudud':448_978,
                  'aholi':33_000_000,
                  'currency':'so\'m'
                  },
    'rossiya':{'poytaxt':'moskva',
                  'hudud':498_448_978,
                  'aholi':133_030_000,
                  'currency':'rubl'
                  },
    'aqsh':{'poytaxt':'vashington',
                  'hudud':23_448_978,
                  'aholi':567_043_000,
                  'currency':'dollar'
                  },
    'fransiya':{'poytaxt':'parij',
                  'hudud':238_945,
                  'aholi':98_000_000,
                  'currency':'frank'
                  }
    } 
# for davlat, data in davlatlar.items():
#     if davlat == 'aqsh':
#         davlat = davlat.upper()
#     else:
#         davlat = davlat.title()
#     print(f"\n{davlat}ning poytaxti {data['poytaxt'].title()}."
#           f"\nHududi: {data['hudud']} kv.km"
#           f"\nAholisi: {data['aholi']}"
#           f"\nPul birligi: {data['currency']}")
    
"""Yuqoridagi dasturga o'zgartirish kiriting: konsolga barcha davlatlarni emas,
foydalanuvchi so'ragan davlat haqida ma'lumot bering. Agar davlat sizning 
lug'atingizda mavjud bo'lmasa, "Bizda bu davlat haqida ma'lumot yo'q" degan 
xabarni chiqaring."""
sorov = input("Qaysi davlat haqida ma'lumotga ega bo'lishni hohlaysiz?>>>").lower()
#tekshirish uhcun qulay ko'rinishga keltirib olamiz
if sorov in davlatlar: #davlatlar.keys() bilan ekvivalent
    data = davlatlar[sorov] # bu qism if dan kynga tushsa xato beradi, chunki, 
    # bunda sorov katta harflarga o'tib qogan bo'ladi
    if sorov == 'aqsh':
        sorov = sorov.upper()
    else:
        sorov = sorov.title()
    print(f"\n{sorov}ning poytaxti {data['poytaxt']}."
          f"\nHududi: {data['hudud']} kv.km ga teng."
          f"\nAholisi: {data['aholi']/1_000_000} million."
          f"\nPul birligi: {data['currency']}")
else:
    print("Bizda bu davlat haqida ma'lumot mavjud emas!")
 
    
# dict.GET(searching_value, exception)
# searching_value - shart tekshiriladigan yoki dictionary dan izlanayotgan qiymat
# exception - errorni ushlash uchun ifoda, agar uni yozmasak, None qiymat qaytadi



    
     
    
    
    
    