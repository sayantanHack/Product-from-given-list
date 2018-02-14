listofnum = [2,4,1,5,6,40,-1]
num = int(input("Which number you want as a product : "))

i=None
j = None
            
for i in range(len(listofnum)):
    if num%listofnum[i]==0:   
        if num/listofnum[i] in listofnum:
            print('The numbers multiplied are : ',listofnum[i],'and',int(num/listofnum[i]))
        
