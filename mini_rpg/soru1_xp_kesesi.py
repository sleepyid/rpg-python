mevcut = int(input("Arden'in mevcut XP'si: "))
goblin = int(input("Yenilen goblin sayısı: "))
kat = int(input("Tamamlanan zindan katı: "))

xp = mevcut + goblin * 37 + (kat ** 2) * 24 + 150

seviye = xp // 1250
kalan_xp = xp % 1250

gumus = goblin * 29 + kat * 340
gumus += seviye * 115

altin = gumus // 24
gumus %= 24

print(f"Toplam XP: {xp}")
print("Atlanan seviye:", seviye, "| Yeni seviyedeki XP:", kalan_xp, end="")
print(f" | Sonraki seviyeye: {1250 - kalan_xp} XP")
print(f"Kese: {altin} altın", f"{gumus} gümüş", sep=" + ")
