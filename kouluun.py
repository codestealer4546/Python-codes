print("Kuinka vanha olet?")
ika = input()
ika = int(ika)

if ika < 7:
    print("Et pääse kouluun")
elif ika > 7 and ika <= 18:
    print("Olet koulussa tai lukiossa")
else:
    print("Olet jo käynyt koulun")