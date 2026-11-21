ilksayi=int(input("Lütfen bir sayı giriniz: "))
ikincisayi=int(input("Lütfen ikinci bir sayı giriniz: "))
islem= input("""Yapmak istediğiniz işlemi giriniz.
(Toplama: +, Çıkarma: -, Çarpma: *, Bölme: /: )
""")

if islem=="+":
    print("Toplama işleminin sonucu: "+  str(ilksayi+ikincisayi))
if islem=="-":
    print("Çıkarma işleminin sonucu: "+  str(ilksayi-ikincisayi))
if islem=="*":
    print("Çarpma işleminin sonucu: "+  str(ilksayi*ikincisayi))
if islem=="/":
    print("Bölme işleminin sonucu: "+  str(ilksayi/ikincisayi))