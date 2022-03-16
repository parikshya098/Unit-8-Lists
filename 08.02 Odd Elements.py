s = input("Enter Values Separated by Space: ")
list1 = s.split(" ")
for x in range(len(list1)):
    if int(list1[x])%2==1:
        print(list1[x])