str_input = input("Enter Values Separated by Spaces: ")
lst_input = list(map(int, str_input.split()))
min_ele = lst_input[0]
max_ele = lst_input[0]
ind_min = 0
ind_max = 0

for i in range(1,len(lst_input)):
    if lst_input[i]<min_ele:
        ind_min = i 
    if lst_input[i]>max_ele:
        ind_max = i
        
t = lst_input[ind_min]
lst_input[ind_min] = lst_input[ind_max]
lst_input[ind_max] = t
print("Swapped Minimum and Maximum:", *lst_input)