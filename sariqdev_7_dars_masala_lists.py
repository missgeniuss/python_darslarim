# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 14:06:59 2021

@author: NewMoon

"""
#ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
ismlar = ['Elmira', 'Madina', 'Marjona']
print("Salom,", ismlar[0] + ",yaxshimisiz?\n", ismlar[1], "ham yaxshi ekanmi?\n", \
      "Yaqin o'rtada", ismlar[2]+"ni ko'rmadingizmi?")

#sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik). 
sonlar = [1, -2.3, 44, 21, 0.6]
print("Dastlabki sonlar or'yxati:", sonlar)
#Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. 
#Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring. 
sonlar[0] = sonlar[0] + 10
sonlar[1] = sonlar[1] - 7.7
sonlar[2] = 10
sonlar[3] = sonlar[3]*3
del sonlar[4]
sonlar.append(0)
print(sonlar)
#t_shaxslar va z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz 
#eng ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi
# tirik bo'lgan shaxslarning ismini kiriting. 
t_shaxslar = ["Alisher Navoi", "Bobur Mirzo", 'Naqshbandiy', "Ulug'bek", 'Ibn Sino']
z_shaxslar = ["Stiv Jobs", 'Anjelena Joli', 'Bratt Pit', 'Ilon Mask']

#Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), quyidagi ko'rinishda chiqaring:
shoirlar = [t_shaxslar.pop(0), t_shaxslar.pop(1)]
texniklar = [z_shaxslar[0], z_shaxslar.pop(len(z_shaxslar)-1)] 

print("Oltin asrlarda yashab o'tgan, xotiralari abadiy qalblarga muhrlangan", shoirlar[0] + \
",", shoirlar[1], "kabi shoirlarimiz she'rlarini tinglab beixtiyor o'sha davrga qaytgandek\
bo'lasan kishi...\n")
print("O'tgan asrning ohirlari, Texnika asrining boshlarida", texniklar[0], "kabilar o'zlarining \
olamshumul ixtirolari bilan dunyoni larzaga solgan bo'lsa,", texniklar[1], "esa yaqin davrda \
charaqlagan quyosh bo'ldi desak mubolag'a bo'lmaydi.")

#friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting. 
friends=[]
print(friends)
friends.append('Elmira')
friends.append('Gulzoda')
friends.append('Madina')
friends.append('Marjona')
friends.append("Hulkar")
friends.append('Gulchehra')
friends.append('Fayyoza')
print(friends)

#Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang. 
friends.remove("Fayyoza")
friends.remove("Gulchehra")
print("Kelolmaydiganlar \
olib tashlandi:", friends)
#Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
friends.insert(0, "Gulmera")
friends.insert(-1, "Nodira")
friends.insert(int(len(friends)/2), "Ismigul")
print("Yangi", friends, "ro'yxati shakllantirildi.")

#Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. 
mehmonlar = []
# .pop() va .append() metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(-2))
aziz_mehmon = friends.pop(1)
mehmonlar.append(aziz_mehmon)
print("Kelgan mehmonlar:", mehmonlar)

