import math
def calculateStats(nums):
  return {
    "avg" : sum(nums)/len(nums),
    "max" : max(nums),
    "min" : min(nums)
  }
