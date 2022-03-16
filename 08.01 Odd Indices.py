str_input = input("Enter Values Separated by Spaces: ")
list_input = list(map(int, str_input.split()))

for i in range(len(list_input)):
    if i%2 != 0:
        print(list_input[i])