import toplama,carpma,bolme,cikarma
num1 = int(input("1. sayı: "))
num2 = int(input("2. sayı: "))
islem = str(input("İşlemi giriniz: "))
match islem:
    case "*":
        print(carpma.carp(num1,num2))
    case "/":
        print(bolme.bolme(num1,num2))
    case "-":
        print(cikarma.cikar(num1,num2))
    case "+":
        print(toplama.toplam(num1,num2))