s=set() #empty set
print(type(s))

#no element can be repeated in sets

e={1,4,5,5,5,5,"harry"}
print(e)

e.add(6)
print(e)
e.remove(1)
print(e)

s1={1,34,78}
s2={44,34,65}
print(s1.union(s2))
print(s1.intersection(s2))