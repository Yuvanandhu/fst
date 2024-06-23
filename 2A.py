#operation on tuples

t1=(1,2,3,4,5)
t2=(6,7,8,9)
print("append=",t1+t2)
print("repeat=",t2*5)
print("negative index=",t1[-2])
print("positve index=",t2[2])
print("t or f")
print("5 in t1=",5 in t1)
print("5 in t2=",5 in t2)
print(t1[1:4])
print(t1[1:])
print(t1[:4])
sub=['tam','eng','mat','sci','soc','python']
print(sub)
sub[0]='biology'
print(sub)
del sub[2]
print(sub)
print(sub.pop(0))
print(sub)
sub.pop()
print(sub)
del sub
print(sub)