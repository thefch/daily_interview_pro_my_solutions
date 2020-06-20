def findPythagoreanTriplets(nums):
    list = [i**2 for i in nums]
    for i in range(0,len(list),1):
        print(list[i])
        for j in range(0,len(list),1):
            total = list[j] + list[i]
            
            if (total) in list and (i is not j):
                print('=>',nums[j],'**2 +',nums[i],'**2 =',total,'**2')
                return True
                
                
               
    return False

print (findPythagoreanTriplets([3, 12, 5, 13]))
