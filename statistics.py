import math
def calculateStats(nums):
    ans = {}
    try: 
        ans["avg"] = sum(nums)/len(nums)
    except:
        ans["avg"] = math.nan
    
    ans["max"] = max(nums)
    
    ans["min"] = min(nums)
    return ans if ans["avg"] != math.nan else {
        "avg":math.nan,
        "min":math.nan,
        "max":math.nan
    }
