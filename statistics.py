import math
def calculateStats(nums):
    ans = {}
    try: 
        ans["avg"] = sum(nums)/len(nums)
    except:
        ans["avg"] = math.nan
    
    ans["max"] = max(nums)
    
    try:
        ans["min"] = min(nums)
    except:
        ans["min"] = math.none
    return ans
