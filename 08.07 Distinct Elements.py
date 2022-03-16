str_input = input("Enter Values Separated by Spaces: ")


#convert the string to a list of integers
#[-9999999] is added to list just for balancing the for loop and maintaining the non-empty condition
lst_input = [-9999999] + list(map(int, str_input.split()))


count = 0

#for loop which iterates from indicies 1 to length of list
for i in range(1, len(lst_input)):
    if lst_input[i] != lst_input[i-1]:
        count += 1
        
#printing the final count of unique integers        
print("Number of Distinct Elements:",count)