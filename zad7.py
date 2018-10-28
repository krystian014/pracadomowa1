import random
mylist=[]
for x in range(10):
  mylist.append(random.randint(1,101))

mylist = [int(x) for x in mylist]
mylist=tuple(mylist)
print ("Tuple")
print (mylist)
print ("Maximum")
print (max(mylist))
print ("Minimum")
print (min(mylist))
input ("Nacisnij dowolny klawisz zeby zakonczyc")
