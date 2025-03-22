def countTargetPairs():
    pairs = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] < target:
                pairs = pairs + 1
    return pairs


nums = [-6,2,5,-2,-7,-1,3] 
target = -2
resultaat = countTargetPairs()
print(resultaat)