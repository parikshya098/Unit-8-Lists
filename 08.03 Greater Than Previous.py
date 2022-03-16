my_list =  input("Enter Values Separated by Spaces: ").split()
my_list=[int(i) for i in my_list]
temp = my_list[0]
n = len(my_list) 
for i in range(1,n):
	if my_list[i]>temp:
		print(my_list[i])
	temp = my_list[i]