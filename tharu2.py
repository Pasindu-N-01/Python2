list1 = input('Enter elements of a list separated by space ')

list1 = list1.split()


for i in range(len(list1)):
    
    list1[i] = int(list1[i])
 
 
for num in list1:
 
    # checking condition
    if num % 2 == 0:
        print(num)
 
   

 
    
        
 
