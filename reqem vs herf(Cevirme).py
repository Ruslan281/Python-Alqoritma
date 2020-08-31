# -*- coding: utf-8 -*-
print("***Reqemleri sozlere ceviren program***")
print("***Programdan cixmaq ucun '0'-ededini terminala daxil edin***")
print("***Xahis olunur sadece 4 reqemli eded daxil edin***")

birler=["","bir","iki","üç","dörd","beş","altı","yeddi","səkkiz","doqquz"]
onlar=["","on","iyirmi","otuz","qırx","əlli","altmış","yetmiş","səksən","doxsan"]
yuzler=["","yüz","iki yüz","üç yüz","dörd yüz","beş yüz","altı yüz","yeddi yüz","səkkiz yüz","doqquz yüz"]
minler=["","min","iki min","üç min","dörd min","beş min","altı min","yeddi min","səkkiz min","doqquz min"]

giris=int(input("4 reqemli ededi daxil edin : "))

s=str(giris)
    
a=(minler[int(s[0])],yuzler[int(s[1])],onlar[int(s[2])],birler[int(s[3])])

print(*a)

        
    
