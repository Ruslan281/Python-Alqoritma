def Cevir(say):
    birler = {"0":"","1":"Bir","2":"Iki","3":"Üç","4":"Dörd","5":"Beş","6":"Altı","7":"Yeddi","8":"Səkkiz","9":"Doqquz"}
    onlar = {"1":"On","2":"İyirmi","3":"Otuz","4":"Qırx","5":"Əlli","6":"Altmış","7":"Yetmiş","8":"Səksən","9":"Doxsan","0":""}
    yuz = ["Yuz"]
    
    if len(say) == 3:
        
        if say[0] == "1":
            oxu = yuz[0]+" "+onlar[say[1]]+ " " + birler[say[2]]
            return oku
       
        if say[0] == "0":
            oxu = onlar[say[1]]+ " " + birler[say[2]]
            return oxu
        
        else:
            oxu = birler[say[0]]+ " " + yuz[0]+ " " + onlar[say[1]]+ " " + birler[say[2]]
            return oxu
    
    if  len(say) == 1:
        
        if say[0] == "0":
            oxu = "Sıfır"
            return oxu
        
        else:
            oxu = birler[say[0]]
            return oku
    
    if len(say) == 2:
        oxu = onlar[say[0]]+ " " + birler[say[1]]
        return oxu
say  =input("Ededi daxil edin :")
print(Cevir(say))
