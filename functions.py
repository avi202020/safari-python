
def add(a: int, b: int) -> int:
    return a + b

print(add(1,2))
print(add("Fred", " Jones"))

def show(a, b, *args, **kwargs):
    print(f"a is {a}, b is {b}")
    print(type(args))
    for a in args:
        print(f"> {a}")
    print(type(kwargs))
    for i in kwargs.items():
        print(i)

show(3, 4, 9, 8, 7, fred="Jones", count=3)
l = [9,8,7]
show(5,4, *l)

print(f"Pi is {2.14 + 1}")