import toplama,carpma,bolme,cikarma,modal
print("islem kısmına toplama için '+', çıkarma için '-', çarpma için '*', bölme için '/', kalanı bulmak için 'kalan' giriniz")
while True:
    num1 = int(input("1. sayı: "))
    num2 = int(input("2. sayı: "))
    islem = str(input("İşlemi giriniz: "))
    match islem:
        case "*":
            answer = carpma.carp(num1,num2)
        case "/":
            answer = bolme.bolme(num1,num2)
        case "-":
            answer = cikarma.cikar(num1,num2)
        case "+":
            answer = toplama.toplam(num1,num2)
        case "kalan":
            answer = modal.mod(num1,num2)
    print(answer)