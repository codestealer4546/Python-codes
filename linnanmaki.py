print("Kuinka pitkä olet senttimetreissä")

pituus = input()
pituus = int(pituus)

if pituus < 120:
    print("Et pääse laitteeseen")
else:
    print("Kuinka vanha olet")

ika = input()
ika = int(ika)

if ika < 12:
    print("Et pääse laitteeseen")
else:
    print("Pääset Raketti-laitteeseen")