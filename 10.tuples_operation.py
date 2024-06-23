#creating a tuple
t1=(1,2,3)
t2=(4,5,6)
print(t1+t2)

#B
t1=(1,2,3)
t2=(4,5,6)
print(t1*4)

# positive index
t1=(1,2,3,4,5,6)
print(t1[3])
print(t1[2])

#negative index
t1=(1,2,3,4,5,6)
print(t1[-2])
print(t1[-5])

#E
t1=(1,2,3,4,5,6,7)
print(t1[1:3])
print(t1[3:])
print(t1[:3])

#F
t1=(1,2,3,4,5,6,7)
print(5 in t1)
print(8 in t1)

#G
subjects=['Tamil','English','Maths','Science','Social']
print(subjects)
subjects[0]='biology'
print(subjects)
del subjects [0]
del subjects