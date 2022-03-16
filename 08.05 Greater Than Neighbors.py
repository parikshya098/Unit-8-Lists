print("Enter string containing integer separated by spaces : ")
numList = list(map(int,input().split())) 
counter = 0
for i in range( 1,len(numList)):
  if ((numList[i-1] < numList[i]) and (numList[i+1] < numList[i])):
    counter += 1
print(counter)