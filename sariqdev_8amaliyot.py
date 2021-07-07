# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 23:25:12 2021

@author: User
"""

# =============================================================================
# """O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
davlatlar = ['Italiya', 'Britaniya', 'Norvegiya', 'O\'zbekiston', 'Tojikiston', 'Pokiston', 'Hindiston', 'Ummon']
print(f"menga ma'lum davlatlar {davlatlar}")
# Ro'yxatning uzunligini konsolga chiqaring
print("Ro'yxatning uzunligi:", len(davlatlar))
# sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
print("Tartiblangan davlatlar nomi:", sorted(davlatlar))
# sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
print(f"Teskari tartiblangan davlatrlar nomlari: {sorted(davlatlar, reverse = True)}")
# Asl ro'yxatni qaytadan konsolga chiqaring
print(f"Asl ro'yxat: \n{davlatlar}")

# reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
davlatlar.reverse() # print() choplash funksiyasidan avval metodlarni amalga oshirib olish kk
print(f"Teskari tartiblangan ro'yxat: {davlatlar}")
# sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
davlatlar.sort()
print("Alifbo tartibida tartiblangan ro'yxat:", davlatlar, "\n")
davlatlar.sort(reverse=True)
print(f"Alifbo tartibidan teskari tartiblangan ro'yxat: {davlatlar}\n")
# 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
juft_sonlar = list(range(120, 1200, 2))
# Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
print("120 dan 1200 gacha juft sonlar yig'indisi:", sum(juft_sonlar), "\n")
# Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
max_val = max(juft_sonlar)
min_val = min(juft_sonlar)
ayirma = max_val - min_val
print("Ro'yxatdagi eng katta son %d va eng kichigi esa %d, ularning ayirmasi esa % d bo'ladi" \
      %(max_val, min_val, ayirma))
# Ro'yxatdagi elementlar sonini hisoblang
num_of_elem = len(juft_sonlar)
print("Ro'yxatdagi elementlar soni %d ga teng\n\n" % num_of_elem)
# Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
print(f"Ro'yxat boshidan 20 ta elementlar: {juft_sonlar[:20]}\n")
print("Ro'yxat o'rtasidan 20 ta element: " + str(juft_sonlar[int(len(juft_sonlar)/2) - 10:len(juft_sonlar)//2+10]) +"\n")
print("ro'yxat ohiridan 20 ta element:", juft_sonlar[-20:], "\n")
# taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
taomlar = ['sho\'rva', 'dimlama', 'osh', 'makaron palov', 'lag\'mon']
# nonushta degan yangi ro'yxatga taomlardan nusxa oling
nonushta = taomlar[:]
# Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing
nonushta.remove('sho\'rva')
del nonushta[3]
nonushta.append('g\'ilak')
nonushta.append('omlet')
# Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
print(f"Taomlar ro'yxati: {taomlar}\n")
print(f"Nonushtaga yeyiladigan taomlar esa: {nonushta}\n")
# Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring."""
nonushta = tuple(nonushta)
print(f"O'zgarmas nonushtamiz {nonushta} hisoblanadi")
#nonushta[0] = "qaymoq va non"
nonushta = list(nonushta)
nonushta[0] = "qaymoq va non"
nonushta = tuple(nonushta)
print("O'zgargan nonushta ro'yxati: " + str(nonushta) + " bo'ldi")

# =============================================================================
