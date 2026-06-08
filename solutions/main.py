# DSA-Arrays-Mastery — Core Solutions
# Author: Kushagra Bansal — Project Lab India

def kadane(nums):
    """Kadane's Algorithm — Maximum Subarray Sum
    Time: O(n) | Space: O(1)
    """
    max_sum = cur = nums[0]
    for x in nums[1:]:
        cur     = max(x, cur + x)
        max_sum = max(max_sum, cur)
    return max_sum

def rotate_array(nums, k):
    """Rotate right by k using reversal trick
    Time: O(n) | Space: O(1)
    """
    n = len(nums); k %= n
    nums.reverse()
    nums[:k] = list(reversed(nums[:k]))
    nums[k:]  = list(reversed(nums[k:]))
    return nums

def subarray_sum_k(nums, k):
    """Count subarrays with sum = k (Prefix Sum + HashMap)
    Time: O(n) | Space: O(n)
    """
    from collections import defaultdict
    count = prefix = 0
    freq = defaultdict(int); freq[0] = 1
    for x in nums:
        prefix += x
        count  += freq[prefix - k]
        freq[prefix] += 1
    return count

def max_window_sum(nums, k):
    """Maximum sum subarray of fixed size k
    Time: O(n) | Space: O(1)
    """
    window = sum(nums[:k]); best = window
    for i in range(k, len(nums)):
        window += nums[i] - nums[i-k]
        best = max(best, window)
    return best

def trap_rain_water(height):
    """Two-pointer approach — Trapping Rainwater
    Time: O(n) | Space: O(1)
    """
    l, r = 0, len(height)-1
    lmax = rmax = water = 0
    while l < r:
        if height[l] < height[r]:
            lmax = max(lmax, height[l])
            water += lmax - height[l]; l += 1
        else:
            rmax = max(rmax, height[r])
            water += rmax - height[r]; r -= 1
    return water

def prefix_sum(nums):
    """Build prefix sum array for O(1) range queries
    Time: O(n) build | O(1) query | Space: O(n)
    """
    pre = [0] * (len(nums)+1)
    for i,x in enumerate(nums): pre[i+1] = pre[i]+x
    def query(l, r): return pre[r+1] - pre[l]  # inclusive
    return pre, query

if __name__ == "__main__":
    print("="*55)
    print("  DSA Arrays Mastery — Project Lab India")
    print("="*55)
    print(f"  Kadane[-2,1,-3,4,-1,2,1,-5,4] = {kadane([-2,1,-3,4,-1,2,1,-5,4])}")
    print(f"  Rotate[1,2,3,4,5,6,7],k=3    = {rotate_array([1,2,3,4,5,6,7],3)}")
    print(f"  SubarraySum[1,1,1],k=2        = {subarray_sum_k([1,1,1],2)}")
    print(f"  MaxWindow[2,1,5,1,3,2],k=3   = {max_window_sum([2,1,5,1,3,2],3)}")
    print(f"  RainWater[0,1,0,2,1,0,1,3]   = {trap_rain_water([0,1,0,2,1,0,1,3,2,1,2,1])}")
    print("="*55)