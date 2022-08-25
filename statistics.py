import math
def calculateStats(nums):
    ans = {}
    try: 
        ans["avg"] = sum(nums)/len(nums)
    except:
        ans["avg"] = math.nan
    
    ans["max"] = max(nums) if len(nums) != 0 else math.nan
    
    ans["min"] = min(nums) if len(nums) != 0 else math.nan
    return ans 
