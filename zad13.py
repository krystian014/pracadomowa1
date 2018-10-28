a = ['a','to-delete','b', 'c','to-delete','to-delete', 'd']
print ("Orginalna lista")
print (a)
print ("Po usunieciu")

a=[elem for elem in a if elem != 'to-delete']
print (a)
input ("Nacisnij dowolny klawisz zeby zakonczyc")
