# Fibonacci Dizisi - n. terimi bulan program

def fibonacci(n):
    if n <= 0:
        return "Lütfen pozitif bir sayı giriniz."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a = 0
        b = 1
        for i in range(3, n + 1):
            c = a + b
            a = b
            b = c
        return b


# Kullanıcıdan veri alma
try:
    n = int(input("Terim Sayısını Giriniz: "))
    sonuc = fibonacci(n)
    print(f"Fibonacci Dizisinin {n}. Terimi: {sonuc}")
except ValueError:
    print("Lütfen geçerli bir tam sayı giriniz.")
