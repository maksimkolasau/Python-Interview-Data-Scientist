a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b)
print(a == c)
# => True
# => True

print(a is b)
print(a is c)
# => True
# => False

print(id(a))
print(id(b))
print(id(c))

