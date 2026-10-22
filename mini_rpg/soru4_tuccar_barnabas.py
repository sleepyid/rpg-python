sinif = input("Sınıf (S/B/O): ")
seviye = int(input("Seviye: "))
altin = int(input("Kesedeki altın: "))
kupon = input("Çaylak kuponu var mı? (E/H): ")

if sinif != "S" and sinif != "B" and sinif != "O":
    print("Tüccar Barnabas bu sınıfı tanımıyor.")
else:
    if sinif == "S":
        esya = "Ejder Pulu Zırh"
        fiyat = 780
        min_seviye = 20
    elif sinif == "B":
        esya = "Yıldız Asası"
        fiyat = 645
        min_seviye = 18
    else:
        esya = "Rüzgâr Yayı"
        fiyat = 512
        min_seviye = 15

    # 1. aşama: sadakat indirimi
    fiyat -= seviye // 5 * 12

    # 2. aşama: çaylak kuponu
    if kupon == "E" and seviye < 30:
        fiyat -= fiyat * 24 // 100
    elif kupon == "E" and seviye >= 30:
        print("Kupon yalnızca 30. seviyenin altındakiler içindir, uygulanmadı.")

    print(f"{esya} için son fiyat: {fiyat} altın")

    if seviye < min_seviye:
        print(f"Seviyen yetmiyor: {min_seviye - seviye} seviye daha kas.")
    elif altin >= fiyat:
        print(f"Satın alındı! Kesede kalan: {altin - fiyat} altın")
    elif fiyat - altin <= 50:
        print(f"Barnabas: {fiyat - altin} altını veresiye yazdım, hayırlı olsun!")
    else:
        print(f"Altının yetmiyor: {fiyat - altin} altın eksik.")