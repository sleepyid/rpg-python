eylem = input("Eylem: ")

match eylem:
    case "saldır" | "vur":
        zar = int(input("Zar (1-20): "))
        if not (1 <= zar <= 20):
            print("Zar 1 ile 20 arasında olmalı.")
        else:
            if zar == 20:
                print("KRİTİK VURUŞ! Gölge Lordu 96 hasar aldı.")
            elif zar == 1:
                print("Kılıç elinden kaydı! Hasar yok.")
            else:
                print(f"Gölge Lordu {zar * 4 + 7} hasar aldı.")
    case "iksir":
        can = int(input("Şu anki can: "))
        yeni = 100 if can + 35 > 100 else can + 35
        print(f"İksir içildi. Yeni can: {yeni}")
    case "kaç" | "kac":
        zar = int(input("Zar (1-20): "))
        print("Gölgelerin arasından sıvışıp kaçtın!" if zar >= 14 else "Kaçamadın, Gölge Lordu yolu kesti!")
    case "envanter":
        print("Çanta: Paslı kılıç, meşe kalkan, 3 ekmek, 1 harita parçası.")
    case _:
        print("Arden bu eylemi anlamadı ve sırasını kaybetti.")