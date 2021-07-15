# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 14:06:48 2021

@author: User
"""

# SON TOPISH O'YINI
"""
1) foydalanuvchidan son topishni so'rash zarur, bunda avval oraliq 
tanlab olinadi. 
2) qiymat tekshirilib, xato bo'lsa katta yoki kichikligi choplanadi
3) son topilganda nechta urinishda topilgani choplanadi. Va kompyuter taklif kiritadi
4) taklif qabul qilingach, kompyuter qiymat qaytarishi kk berilgan oraliqda
5) biz tekshirib shartdagi belgilarni kiritamiz
6) javob topilganda yana nechta urinishda topilgani aytiladi
7) user va computer hisobi taxlil qilinib g'olib aniqlanadi
8) yana o'ynaysizmi deb so'raladi.
"""
import random as r

def user_son_top():
    sanoq = 1
    # taqqosla = '' 
    son = r.sample(list(range(1, 11)), 1).pop()
    # print(son)# sonlar ro'yxatidan 1 ta tasodifiy son tanlaydi
    # bunda ro'yxat qaytaradi shuning un ham pop() funksiyasini ishlatish zarur
    n = int(input("1 dan 10 gacha son o'yladim. Topa olasizmi?\n"))
    while True:
        if n == son:
            break
        elif n<son:
            taqqosla = 'katta'
        else:
            taqqosla = 'kichik' 
        n = int(input(f"Xato, men o'ylagan son {n} dan "
                          f"{taqqosla}roq. Yana harakat qiling:\n"))
        sanoq += 1
    
    print(f"\nTOPDINGIZ! {n} sonini o'ylagan edim. "
              f"{sanoq} ta taxmin bilan topdingiz. Tabriklayman!")
    
    return sanoq   


def comp_son_top():
    print("\n1 dan 10 gacha son o'ylang. Men topishga harakat qilaman.")
    taklif = input("Son o'ylagan bo'lsangiz istagan tugmani bosing.")
    if taklif or taklif == "": # istagan tugmani bosish sharti
        comp_sanoq = 1
        sonlar = list(range(1, 11))
        son = r.sample(sonlar, 1).pop()
        while True:
            javob = input(f"Siz {son} sonini o'yladingiz: "
                  f"to'g'ri (T), men o'ylagan son bundan kattaroq (+), "
                  f"yoki kichikroq (-)???")
            if javob.lower() == 't':
                print(f"\n{son} soningizni {comp_sanoq} ta taxminda topdim!")
                break
            if javob == "+":
                for i in sonlar[:]: # bu yerda sonlar dan nusxa oldik
                    if i<=son:
                        sonlar.remove(i)
                print(sonlar)
                son = r.sample(sonlar, 1).pop()
            if javob == "-":
                for i in sonlar[:]:
                    if i>=son:
                        sonlar.remove(i)
                print(sonlar)
                son = r.sample(sonlar, 1).pop()
            
            comp_sanoq += 1
    return comp_sanoq

def play(x = 10): # standart qiymat berish
    savol = True
    while savol:
        print("\nKeling son topish o'ynaymiz!")
        usanoq = user_son_top()
        csanoq = comp_son_top()
        if usanoq<csanoq:
            print(f"\nSiz {usanoq} ta taxminda topdingiz va yutdingiz!")
        elif usanoq>csanoq:
            print(f"\nMen {csanoq} ta taxminda, siz esa {usanoq} ta taxminda topdingiz!"
                  '\nYutqazdingiz!')
        else:
            print("\nDurrang! Ikkimiz ham {csanoq} ta natija bilan topdik")
        savol = int(input("Yana o'ynaymizmi? ha (1)/ yo'q (0)>>>"))

play()
