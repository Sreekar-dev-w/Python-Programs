def rotate_list(nums,k):
    n=len(nums)
    if n==0: return 
    k=k%n
    def reverse(start,end):
        while start<end:
            temp=nums[start]
            nums[start]=nums[end]
            nums[end]=temp
            start+=1
            end-=1
    reverse(0,k-1)
    reverse(k,n-1)
    reverse(0,n-1)
    
    
    
my_list=[1,2,3,4,5]
rotate_list(my_list,2)
print(my_list)