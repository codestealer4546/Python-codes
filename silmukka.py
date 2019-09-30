numero = 0

print("Kuinka ison pyramidin haluat?")
vastaus = input()
vastaus = int(vastaus)
while numero <= vastaus:
    print("O" * numero)
    numero = numero + 1 