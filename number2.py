x = True
print(x)

print(str(True))
print(int(True))

# if (1):
# if ([]):
if ([1,2]):
    print("truthy")
else:
    print("falsy")

l = [0, 1, 2, 3, 4, 5, 6, 7]
print(type(l))
print(l)
print(l[0])

# print(l[len(l)-1])
print(l[-2])

print(l[3:6])
print(l[2:8:2]) # make a new list, starting at index 2, ending "before" index 8, taking every second element
print(l[::2])

l[2] = 99
print(l)
# print(l[99])
# l[99] = 99

l.sort()
print(l)
l.sort(reverse=True)
# l.sort(key=..., reverse=True)
print(l)
print(type(l.sort()))
