import random 

vastauslista = ["Kyllä", "Ei", "Ehkä", "En tiedä", "Kysy uudestaan myöhemmin"]

while True:
    print("Kysy jotain")
    vastaus = input()
    koneenvastaus = random.choice(vastauslista)
    print(koneenvastaus)