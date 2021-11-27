list = [1, 0, 1]
str = ''.join(map(str, list))
#str = ''.join(str(e) for e in list)
print(str)
d = int(str, 2)
print(d)