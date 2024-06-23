L1=[1,2,3]
L2=[4,5,6]
print(L1+L2)
L1=[1,2,3]
print(L1*3)
L1=[1,2,3]
print(L1[0])
print(L1[-3])
print(L1[1])
print(L1[2])
#2 one
L3=[1,2,3,4,5,6,7,8,9,10]
print(L3[1:])
print(L3[:3])
print(L3[1:4])
print(L3[-5:-3])
print(4 in L3)
print(12 in L3)
print(15 in L3)
print(10 in L3)

#t
subjects=['tamil','english','maths','biology','computer science']
del subjects[0]
print("after deleted subjects[0]:",subjects)
subjects[0]="biology"
print("after updated subjects[0]:",subjects)
subjects.remove("maths")
print("after subjects.remove(\"maths\"):",subjects)
print(subjects.pop(0))
print("after subjects.pop(0):",subjects)
subjects.pop()
print("after subjects.pop():",subjects)
del subjects
print("subjects")