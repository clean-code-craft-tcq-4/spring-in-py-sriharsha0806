import math
def calculateStats(nums):
  ans = {}
  try: 
    ans["avg"] = sum(nums)/len(nums)
  except:
    ans["avg"] = math.nan
  try:
    ans["max"] = max(nums)
  except:
    ans["max"] = math.nan
  try:
    ans["min"] = min(nums)
  except:
    ans["min"] = math.none
  return ans
