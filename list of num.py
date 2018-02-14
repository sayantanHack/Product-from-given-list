listofnum = [2,4,1,5,6,40,-1]
num = int(input("Which number you want as a product : "))

i=None
j = None
for i in range(len(listofnum)):     # for the 1st itteration
    for j in range(len(listofnum)):  # second itteration
        if num/listofnum[i] == listofnum[j]:
            print ("The numbers are: ",listofnum[i],'and',listofnum[j])
            
            
    
