import copy

l1 = [1, 3, 5]
l2 = l1[:]
l3 = copy.copy(l1)

print(id(l1))
print(id(l2))
print(id(l3))

l1.append("ahah")
print(id(l1))
print(id(l2))
print(l1)
print(l2)
print(l3)