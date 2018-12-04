from collections import Counter

a = [(1, 2), (1, 3), (1, 4)]

b = Counter(a)

print(b)

b.update(list((1, 5)))

print(b)
