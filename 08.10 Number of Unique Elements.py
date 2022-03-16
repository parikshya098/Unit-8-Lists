n = input('Enter Values Separated by Spaces: ').split()
l=[]
for i in range(0, len(n)):
   c = 0
   for j in range(0, len(n)):
       if(i != j and n[i] == n[j]):
           c += 1
   if(c == 0):
       l.append(n[i])
print('Unique Elements:',*l)