# Dört Ardışık Terimde Eksik Olan Değeri Bulma

def eksik_terim_bul(dizi):
    # Sayıları küçükten büyüğe sıralıyoruz
    dizi.sort()
    
    # Olası ortak farkları bul
    farklar = []
    for i in range(len(dizi) - 1):
        farklar.append(dizi[i+1] - dizi[i])
    
    # En küçük fark genelde gerçek ortak farktır
    ortak_fark = min(farklar)
    
    # Eksik terimi bul
    for i in range(len(dizi) - 1):
        if dizi[i+1] - dizi[i] != ortak_fark:
            return dizi[i] + ortak_fark
    
    return "Eksik terim bulunamadı."


# Kullanıcıdan veri alma
try:
    giris = input("Dört ardışık terimden üç tanesini boşlukla giriniz: ")
    sayilar = list(map(int, giris.split()))
    
    if len(sayilar) != 3:
        print("Lütfen tam olarak 3 sayı giriniz.")
    else:
        sonuc = eksik_terim_bul(sayilar)
        print("Eksik Olan Değer:", sonuc)

except ValueError:
    print("Lütfen sadece tam sayı giriniz.")
