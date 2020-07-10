
class Date:
    # pass # {}
    def __init__(self, day, month, year=2020):
        self.day = day
        self.month = month
        self.year = year
        Date.classvar= "I'm date stuff"

    def __str__(self):
        return f"Date day is {self.day}, month is {self.month}, year is {self.year}"

    def __repr__(self):
        return self.__str__()
        # return "Repr: I'm supposed to be a date..."

    def do_stuff(self):
        print(d.day, " is a lovely day")

    @staticmethod
    def do_static_stuff():
        print("hello")

d = Date(1,2,3) # constructs and initializes...
print(type(d))
print(d)

ld = [Date(month=7, day=10), Date(1, 2, 1920)]
print(ld)

d.do_stuff()
Date.do_static_stuff()
d.do_static_stuff()

print(Date.classvar)

class Holiday(Date):
    def __init__(self, day, month, year, name):
        super().__init__(day, month, year)
        self.name = name

    def __str__(self):
        return f"Holiday called {self.name} {super().__str__()}"

h = Holiday(1,1, 2021, "New Year's Day")
print(h)

