import random
mylist=[]
for x in range(6):
  mylist.append(random.randint(1,101))

mylist = [int(x) for x in mylist]
mylist.sort()
print ("Posortowana lista szesciu losowych liczb")
print (mylist)
input ("Nacisnij dowolny klawisz zeby zakonczyc")
