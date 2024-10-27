#brute force
def leaders(num1):
    lead=float('-inf')
    leaders=[]
    for i in range(len(num1)):
        lead=0
        for j in range(i+1,len(num1)):
            if num1[i]>num1[j]:
                lead=num1[i]
            else:
                lead=0
                break
        if lead>0:
            leaders.append(lead)
    if num1[-1]>0:
        leaders.append(num1[-1])
    return leaders
mylist=[16,17,4,5,1,2]    
print("leaders of the array is : ",leaders(mylist))

#optimal soltion
def Leaders(num1):
     last=len(num1)-1
     left=last-1
     lead=0
     leaders=[]
     while left>=0:
         if num1[last]<num1[left]:
             leaders.append(num1[left])
             last=left
             left-=1
         else:
             left-=1
     return leaders
 
mylist=[10,9,8,7,6,5 ]    
print("leaders of the array is : ",leaders(mylist))   
        