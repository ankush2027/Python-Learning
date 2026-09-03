#Swap elements at the index
nums=[10, 20, 30, 40, 50]
nums[1],nums[4]=nums[4],nums[1]
print(nums)


#In place
def square(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2
    return nums



#Two pointer + swap
def two_pointer(nums):
    left=0
    right=len(nums)-1
    while left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1
    return nums



nums=[1,2,3,4,5]
result1=square(nums)
result2=two_pointer(nums)

print(result1)
print(result2)


