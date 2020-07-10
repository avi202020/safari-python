x = (1,2,3,)
print(type(x))
print(x)
print(x[0])
print(x[0:2])

x = 9, 8, 7
print(type(x))
print(x)
a, b, c = x
print(a, b, c)

def get_tuple():
    return 1,2,3

print(get_tuple())
# a, b, c, d = get_tuple()
print(a, b, c)

a,b,c = [1,2,3]
l = [1,2,3]
print("from list", a,b,c)

tup = (1,"two",3)
print(tup)

l[1] = 99
print(l)

# tup[1] = 99

aset = {1,2,3,3,2,1,0}
print(aset)

dict = {"Fred" : "Jones", "Jim" : "Smith"}
print(dict)
print(type(dict))
print(dict["Fred"])
# print("missing", dict["missing"])
dict["Alice"] = "Smith"
dict["Fred"] = "Williams"
print(dict)