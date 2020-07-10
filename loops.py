
count = 1;

# if count > 2: print("yeah it's big") ; print("I meant it")

while count < 5:
    count += 1
    print("count ", count)
    if count == 3:
        continue
    print(count, "didn't cause a break")
else:
    print("didn't break")

