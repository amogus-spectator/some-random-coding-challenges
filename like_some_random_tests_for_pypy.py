import time
def total_of_a_num(n:int)->int:
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum
p1 = time.perf_counter()
print(total_of_a_num(1_000_000))
p2 = time.perf_counter()
print(f"Time taken = {p2-p1}")

def bubble_sort(nums:list)->list:
    for i in range(len(nums)):
        for j in range(len(nums)-i-1):  # -1 because last element is sorted
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
    return nums

p1 = time.perf_counter()
print(bubble_sort([15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]))
p2 = time.perf_counter()
print(f"Time taken = {p2-p1}")