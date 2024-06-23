s1={1,2,3,4,5}
s2={4,5,6,7}

s=s1.union(s2)
print("s1.union(s2)=",s)
s=s2.union(s1)
print("s2.union(s1)=",s)

s=s1.intersection(s2)
print("s1.intrsection(s2)=",s)
s=s2.intersection(s1)
print("s2.intersection(s1)=",s)

s=s1.difference(s2)
print("s1.difference(s2)=",s)
s=s2.difference(s1)
print("s2.difference(s1)=",s)

s=s1.symmetric_difference(s2)
print("s1.symmetric_difference(s2)=",s)
s=s2.symmetric_difference(s1)
print("s2.symmetric_difference(s1)=",s)