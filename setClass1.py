'''s1 = {1,2,5,6}
s2 = {3,2,6,7}
#union
#s1 = s1.union(s2)
s1.update(s2)
#print(s1.union(s2)
print(s1,s2)'''

#intersection
'''#s1 = s1.intersection(s2)
s1.intersection_update(s2)
#print(s1.intersection(s2))
print(s1,s2)'''

#difference
#print(s1.difference(s2))
#isdisjoint
cities = {"tokyo","madrid","delhi"}
cities2 = {"seoul","madrid","tokyo","delhi"}
#print(cities.isdisjoint(cities2))

'''print(cities.issubset(cities2))
print(cities2.issuperset(cities))


cities.add("meerut")
print(cities)

cities.discard("meerut")
print(cities)

cities.pop()
print(cities)

#del cities
cities.clear()
print(cities)'''

if "tokyo" in cities2:
    print("element is present..")
else:
    print("element is not present..")


for i in cities2:
    print(i)
















