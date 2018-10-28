a=input ("Podaj pierwsza liczbe ")
a=float(a)
znak=input ("Podaj znak operacji ")
b=input ("Podaj druga liczbe ")
b=float(b)

if znak=='+':
    y=a+b
    print ("Suma " + str(y))
elif znak=="-":
    print ("Roznica " + str(a-b))
elif znak=="*":
    print ("Wynik " + str(a*b))
elif znak=="/":
    if b==0:
        print ("Nie mozna dzielic przez 0")
    else:    
        print ("Wynik " + str(a/b))
input ("Nacisnij klawisz zeby wyjsc ")
