locker = [bool(1)] * 100
# create an empty list, to denote all the locker, the locker is all open after first student come
# now we got a list type data locker of 100 true, which is the situation after the first student's action
for s in range(2, 101):
    # we're now modeling 3 to 100 students situation by for loop, select them out and reverse the state of locker
    for i in range(0, 100):
        if i % s == s - 1:  # this line is translating the relation between student Sn and their changing lock action
            if locker[i]:  # this line mean change the true to false
                locker[i] = bool(0)
            else:  # this line mean change false to true
                locker[i] = bool(1)
print("opened lockers number ordinal number : ")
for n in range(0, 100):
    count=0
    if locker[n]:
        count += 1
        print(n + 1, sep=",",end=" ")
        if count%10==0:
            count += 1
            print()




