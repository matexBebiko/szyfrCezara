MAX_KEY = 26
MIN_KEY = 1
def szyfr_cezara(haslo, klucz):
    zaszyfrowaneHaslo = ""
    for i in haslo:
        litera = klucz + ord(i)
        if litera > ord('z'):
             litera -= 26
        elif litera < ord('a'):
            litera +=26
        zaszyfrowaneHaslo += chr(litera)
    return zaszyfrowaneHaslo
def main():
    twojeHaslo = input("Podaj hasło: ")
    while True:
        klucz = int(input("Podaj klucz: 🔧"))
        if klucz > MAX_KEY and klucz < MIN_KEY:
            print("Wartość kluczna musi byćod 1 do 26")
        else:
            cezar = szyfr_cezara(twojeHaslo, klucz)
            print(f"Twoje hasło {cezar}")
            break
main()