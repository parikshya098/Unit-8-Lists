str_input = input("Enter Values Separated by Spaces: ")
lst_input = [-9999999] + list(map(int, str_input.split()))
count = 0

for i in range(1, len(lst_input)):
    if lst_input[i] != lst_input[i-1]:
        count += 1    
print("Number of Distinct Elements:",count)