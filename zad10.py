poczatek=1
poczatek=int(poczatek)
ostatnia=100
ostatnia=int(ostatnia)
podzielne = []
for testowana in range(poczatek, ostatnia):
    if testowana % 7 == 0:
        podzielne.append(testowana)

print ("Lista liczb podzielnych przez 7:")
print (podzielne)
input ("Nacisnij dowolny klawisz zeby zakonczyc")
