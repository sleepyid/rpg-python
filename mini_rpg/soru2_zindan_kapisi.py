seviye = int(input("Arden'in seviyesi: "))
can = int(input("Can puanı (0-100): "))
iksir = int(input("Çantadaki iksir sayısı: "))

if seviye < 1 or seviye > 60:
    print("HATA: Seviye 1 ile 60 arasında olmalı.")
elif can < 24 and iksir == 0:
    print("Zindan kapısı kapandı: Önce kasabaya dönüp dinlen.")
elif seviye >= 45 and can >= 70:
    print("Ejderha Mağarası'nın kapısı açıldı!")
elif 30 <= seviye < 45 and (can >= 50 or iksir >= 2):
    print("Örümcek Ormanı seni bekliyor.")
elif seviye >= 10:
    print("Goblin Mahzeni: Isınma turu için ideal.")
else:
    print("Daha çok çaylaksın: Köy çevresinde tavşan avla.")