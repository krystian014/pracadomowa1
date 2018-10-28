print ("Prosze odpowiadac na pytania bez uzycia polskich znakow.")

odp1=input ("Jakie jezyk programowania uczymy sie na kursie? ")
odp1=str.lower(odp1)
punkty="0"
punkty=int(punkty)
klucz1="python"

if odp1==klucz1:
    punkty=punkty+1

odp2=input ("Czy uzywamy komputera na zajeciach? ")
odp2=str.lower(odp2)
klucz2="tak"

if odp2==klucz2:
    punkty=punkty+1

odp3=input ("Czy programujemy na zajeciach? ")
odp3=str.lower(odp3)
klucz3="tak"

if odp3==klucz3:
    punkty=punkty+1

odp4=input ("Czy pracujemy w grupach? ")
odp4=str.lower(odp4)
klucz4="nie"

if odp4==klucz4:
    punkty=punkty+1

odp5=input ("Czy uczymy sie pythona 1? ")
odp5=str.lower(odp5)
klucz5="nie"

if odp5==klucz5:
    punkty=punkty+1    

odp6=input ("Czy uczymy sie pythona 3.7? ")
odp6=str.lower(odp6)
klucz6="tak"

if odp6==klucz6:
    punkty=punkty+1

odp7=input ("Czy mamy prace domowe? ")
odp7=str.lower(odp7)
klucz7="tak"

if odp7==klucz7:
    punkty=punkty+1

odp8=input ("Czy musimy zrobic prezentacje? ")
odp8=str.lower(odp8)
klucz8="nie"

if odp8==klucz8:
    punkty=punkty+1

odp9=input ("Czy to zajecia indywidualne? ")
odp9=str.lower(odp9)
klucz9="nie"

if odp9==klucz9:
    punkty=punkty+1

odp10=input ("Czy musimy przyniesc swoje komputery? ")
odp10=str.lower(odp10)
klucz10="tak"

if odp10==klucz10:
    punkty=punkty+1

wynik=(punkty/10)*100
print ("Wynik: " + str(wynik) + "%")   
    
input ("Nacisnij klawisz zeby wyjsc ")
