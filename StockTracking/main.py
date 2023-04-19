fiyat = {"Muz":"4","Elma":"2","Portakal":"1.5","Armut":"3"}
stok = {"Muz":"6","Elma":"8","Portakal":"32","Armut":"15"}
counter =0
toplam =0
while(counter <3):
    toplam =0
    counter = counter +1
    kinds= int(input("Welcome... How many kinds of fruit would you like to buy?"))
    while(kinds >0):
        kinds = kinds -1
        fruit= input("Which fruit would you like to buy?")
        number =int(input("How many would you like to buy?"))
        if fruit in fiyat.keys():
            if(number <= int((stok[fruit]))):
                toplam = float(toplam + int(toplam) + int(number) * float(fiyat[fruit]))
                stok.update({fruit : int((stok[fruit]))-int(number)})
            elif(number > int((stok[fruit]))):
                print("Yetersiz Stok Daha az ürün girin")
                number = input("How many would you like to buy?")
                stok.update({fruit: int((stok[fruit])) - int(number)})
                toplam = toplam + int(number) * int((fiyat[fruit]))
            else:
                print("Stok bitmiştir.")
    print("Odenecek Tutar:",end="")
    print(toplam)







