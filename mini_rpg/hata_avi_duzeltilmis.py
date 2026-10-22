seviye = int(input("Karakter seviyesi: "))
sinif = input("Sınıf (S/B/O): ")
can = int(input("Can puanı: "))
if seviye >= 10 and can >= 50:
    print("Zindana girebilirsin.")
else:
    print("Önce biraz antrenman yap.")
if sinif == "S":
    bonus = seviye * 3
elif sinif == "B":
    bonus = seviye * 2
else:
    bonus = seviye
if seviye == 60:
    print("Maksimum seviyedesin, efsane oldun!")
print("Saldırı bonusu: " + str(bonus))
