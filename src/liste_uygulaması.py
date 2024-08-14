# Görevleri saklamak için boş bir liste oluşturuyoruz
to_do_list = []

def gorev_ekle(gorev):
    to_do_list.append(gorev)
    print(f"'{gorev}' görevi eklendi.")
def gorev_sil(gorev):
    if gorev in to_do_list:
        to_do_list.remove(gorev)
        print(f"'{gorev}' görevi silindi.")
    else:
        print(f"'{gorev}' görevi listede bulunamadı.")

def gorevleri_goruntule():
    if to_do_list:
        print("Görev Listesi:")
        for i, gorev in enumerate(to_do_list, 1):
            print(f"{i}. {gorev}")
    else:
        print("Görev listesi boş.")

while True:
    print("\nTo-Do Listesi Uygulaması")
    print("1. Görev Ekle")
    print("2. Görev Sil")
    print("3. Görevleri Görüntüle")
    print("4. Çıkış")
    
    secim = input("Bir seçenek seçin: ")
    
    if secim == '1':
        gorev = input("Eklenecek görevi girin: ")
        gorev_ekle(gorev)
    elif secim == '2':
        gorev = input("Silinecek görevi girin: ")
        gorev_sil(gorev)
    elif secim == '3':
        gorevleri_goruntule()
    elif secim == '4':
        print("Uygulama kapatılıyor.")
        break
    else:
        print("Geçersiz seçim.")
