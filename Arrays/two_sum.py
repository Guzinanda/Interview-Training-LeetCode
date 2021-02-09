'''
@   Two Sum | 01

@   Problem
    Given an array of integers nums and an integer target, return indices of the two 
    numbers such that they add up to target. Assume that each input would have exactly 
    one solution, and you may not use the same element twice.

@   Example
    Input:  nums = [2,7,11,15], target = 9
    Output: [0,1]

@   Template

'''

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    d = {}                              # {11:0, 15:1, 2:2, 7:3}

    for i, num in enumerate(nums):      # [(0, 2),(1,7),(2,11),(3,15)]

        m = target - num

        if m in d:
            return [d[m], i]
        
        else:
            d[num] = i


# TEST _______________________________________________________________________________

nums = [2,7,11,15]
target = 9

print(twoSum(nums, target))