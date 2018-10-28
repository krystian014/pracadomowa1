poczatek=input("Podaj poczatek zakresu testowanych liczb: ")
poczatek=int(poczatek)
ostatnia=input ("Podaj koniec zakresu testowanych liczb: ")
ostatnia=int(ostatnia)
podzielne = []
for testowana in range(poczatek, ostatnia):
    if testowana % 5 == 0:
        podzielne.append(testowana)

print ("Lista liczb podzielnych przez 5:")
print (podzielne)
input ("Nacisnij dowolny klawisz zeby zakonczyc")

