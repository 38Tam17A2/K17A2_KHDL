def has_lucky_number(nums):
    for num in nums:
        if num % 7 == 0:
            return True
    return False
nums=[2,6,7,9]
S=has_lucky_number(nums)
print(S)