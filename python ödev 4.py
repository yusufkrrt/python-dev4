import sqlite3

baglanti = sqlite3.connect('metinler.db')
imlec = baglanti.cursor()

imlec.execute('''
CREATE TABLE IF NOT EXISTS metinler (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    metin TEXT
)
''')

metin1 = input("Birinci metni girin: ")
metin2 = input("İkinci metni girin: ")

imlec.execute("INSERT INTO metinler (metin) VALUES (?)", (metin1,))
imlec.execute("INSERT INTO metinler (metin) VALUES (?)", (metin2,))
baglanti.commit()

def kelime_benzerligi_hesapla(metin1, metin2):
    kume1 = set(metin1.lower().split())
    kume2 = set(metin2.lower().split())

    kesisim = kume1.intersection(kume2)
    birlesim = kume1.union(kume2)

    benzerlik_orani = len(kesisim) / len(birlesim)

    return benzerlik_orani, kesisim

def karakter_benzerligi_hesapla(metin1, metin2):
    kume1 = set(metin1.lower().replace(" ", ""))
    kume2 = set(metin2.lower().replace(" ", ""))

    kesisim = kume1.intersection(kume2)
    birlesim = kume1.union(kume2)

    benzerlik_orani = len(kesisim) / len(birlesim)

    return benzerlik_orani, kesisim

benzerlik_orani_kelime, benzer_kelime_seti = kelime_benzerligi_hesapla(metin1, metin2)
benzerlik_orani_karakter, benzer_karakter_seti = karakter_benzerligi_hesapla(metin1, metin2)

benzer_kelime_listesi = sorted(list(benzer_kelime_seti))
benzer_karakter_listesi = sorted(list(benzer_karakter_seti))

print(f"Kelime tabanlı benzerlik oranı: {benzerlik_orani_kelime:.2f}")
print("Benzer kelimeler:", ", ".join(benzer_kelime_listesi))

print(f"Karakter tabanlı benzerlik oranı: {benzerlik_orani_karakter:.2f}")
print("Benzer karakterler:", ", ".join(benzer_karakter_listesi))

with open("benzerlik_durumu.txt", "w") as f:
    f.write(f"Kelime tabanlı benzerlik oranı: {benzerlik_orani_kelime:.2f}\n")
    f.write("Benzer kelimeler: " + ", ".join(benzer_kelime_listesi) + "\n")
    f.write(f"Karakter tabanlı benzerlik oranı: {benzerlik_orani_karakter:.2f}\n")
    f.write("Benzer karakterler: " + ", ".join(benzer_karakter_listesi))

baglanti.close()
