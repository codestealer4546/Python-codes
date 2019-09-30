pisteet = 0

def kysy_kysymys(kysymys, oikea_vastaus):
    global pisteet
    print(kysymys)
    vastaus = input()
    if vastaus == oikea_vastaus:
        print("Oikein")
        pisteet = pisteet + 1
    else:
        print("Väärin")

kysy_kysymys("Kuinka monta kieltä on kitarassa", "6")
kysy_kysymys("Mikä on Suomen presidentin koiran nimi", "Lennu")
kysy_kysymys("Kuka on Suomen presidentti", "Sauli Niinistö")

print("Sait {} pistettä".format(pisteet))