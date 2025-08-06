#You are given an integer array heights where heights[i] represents the height of the ith bar.
#You may choose any two bars to form a container. Return the maximum amount of water a container can store.

#Example 1: Input: height = [1,7,2,5,4,7,3,6]
#Output: 36  ( 7 and 6, actual height = smaller ele -> 6. Then width = 7's indice - 6's indice = 7 - 1 = 6. Area = 6 * 6.

#Brute Force: O(n)^2
res=0
for i in range(len(heights)-1):
    for j in range(i+1, len(heights)):
        height=min(heights[i],heights[j])
        width=j-i
        amt=height*width
        if amt>res:
            res=amt
return res

#Two pointers: O(n)
res=0
i,j=0,len(heights)-1

while(j>i):
    width=j-i
    height=min(heights[i],heights[j])
    area=height*width
    if area>res:
        res=area
    if heights[i]<heights[j]:
        i+=1
    else:
        j-=1
    
return res
