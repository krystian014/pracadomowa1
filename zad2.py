ostatnia=input ("Podaj do jakiej liczby od 0 program ma szukać liczb piewszych: ")
ostatnia=int(ostatnia)
pierwsze = []
for testowana in range(2, ostatnia):
    
    jestPierwsza = True
    for num in range(2, testowana):
        if testowana % num == 0:
            jestPierwsza = False
            break
      
    if jestPierwsza:
        pierwsze.append(testowana)

print ("Lista liczb pierwszych:")
print (pierwsze)
input ("Nacisnij dowolny klawisz zeby zakonczyc")
