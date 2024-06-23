capitals={"usa":"washington .d.c","france":"paris","india":"new delhi"}
print(capitals)
print(type(capitals))

#unique keys
numnames={1:"one",2:"two",3:"three",2:"two",1:"one",2:"two"}
print(numnames)

#dict()constructor method
numdict=dict(I='one',II='two',III='three')
print("numdict=",numdict)
print(type(numdict))
empty=dict()
print("empty=",empty)
print(type (empty))

#get dictionary values
numnames={1:"one",2:"two",3:"three"}
print(numnames[1],numnames[2],numnames[3])

#none
capitals={"usa":"washington d.c","france":"paris","india":"new delhi"}
print(capitals["usa"],capitals["france"])

#update value of key
capitans={"england":"root","australia":"smith","india":"dhoni"}
capitans['india']='virat'
capitans['australia']='paine'
print(capitans)

#add new key value of pair
capitans={"england":"root","india":"virat"}
capitans['south africa']='plessis'
print(capitans)

#delete a key value  pair
capitans={"australia":"smith","india":"dhoni","srilanka":"jayasuriya"}
del capitans['srilanka']
print(capitans)

#retrive dictionary keys and values
d1={'name':'steve','age':21,'marks':60,'course':'computer science'}
print(d1.keys())
print(d1.values())

#check keys
capitans={'england':'root','australia':'paine','india':'virat','srilanka':'jayasuriya'}
b='england'in capitans
print (b)
b='india'in capitans
print (b)
b='france' in capitans
print (b)

#acess dictionary using  for loop
capitals={"usa":"washington d.c","france":"paris","india":"new delhi"}
for key in capitals:
    print( "key = "+key+",value = "+capitals [key])
