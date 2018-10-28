mylist=range(1,11)
mylist = [int(x) for x in mylist]
print ("Pierwotna lista:")
print (mylist)
mylist.sort(reverse=True)
print ("Odwrotna lista:")
print (mylist)
input ("Nacisnij dowolny klawisz zeby zakonczyc")
