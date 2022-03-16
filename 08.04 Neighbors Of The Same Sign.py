string_of_nums = input('Enter Values Separated by Spaces: ')
y = [int(q) for q in string_of_nums.split()]
for i in range(len(y)-1):
    if y[i] >= 0 and y[i+1] >=0: 
        print(y[i] ,y[i+1])   
    elif y[i] < 0 and y[i+1] <0: 
        print(y[i] ,y[i+1])   