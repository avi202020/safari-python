
l = [1,2,3,4]

def timestwo(x):
    return x * 2

# l2 = list(map(timestwo, l))

l2 = list(map(lambda x: x * 4, l))
print(l2)

l3 = [x ** 2 for x in l]
print(l3)

from math import modf
from math import sqrt

print(modf(3.14))
print([x ** 2 for x in range(2, 10, 2)]) # map, and filter
print([x ** 2 for x in range(1, 10) if modf(x/2)[0] == 0]) # map, and filter

print([(a, o, sqrt(a**2+o**2)) for a in range(1, 15) for o in range(a, 15) if modf(sqrt(a**2+o**2))[0] == 0])

# New with python 3.8 "walrus" operator aka "assignment operator"
if ((a := 5) == 5):
    print("yay!")

print([(a, o, h) for a in range(1, 15) for o in range(a, 15) if modf(h := sqrt(a**2+o**2))[0] == 0])

