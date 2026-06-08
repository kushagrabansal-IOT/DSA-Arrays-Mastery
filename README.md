# DSA-Arrays-Mastery 🚀

[![Python](https://img.shields.io/badge/Language-Python_3.11-3776ab?style=flat&logo=python&logoColor=white)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-22c55e?style=flat)](LICENSE)
[![DSA](https://img.shields.io/badge/Category-DSA-f97316?style=flat)](#)
[![Stars](https://img.shields.io/github/stars/kushagrabansal-IOT/DSA-Arrays-Mastery?style=social)](https://github.com/kushagrabansal-IOT/DSA-Arrays-Mastery)
[![Interview Ready](https://img.shields.io/badge/Interview-Ready-7c3aed?style=flat)](#)

> Master arrays with 50+ problems — traversal, rotation, prefix sum, Kadane's algorithm, sliding window. Interview-ready with complexity analysis and test cases.

**Built by [Kushagra Bansal](https://github.com/kushagrabansal-IOT) | Founder @ Project Lab India, Jaipur**

---

## 📌 Topics Covered

| # | Topic | Problems Covered |
|---|-------|-----------------|
| 1 | Array Traversal | Linear scan, Two-pass |
| 2 | Insertion & Deletion | Shift operations, In-place |
| 3 | Array Rotation | Left/Right by K, Reversal trick |
| 4 | Prefix Sum | Range sum query, Subarray sum |
| 5 | Sliding Window | Fixed + variable window |
| 6 | Kadane's Algorithm | Max subarray, Max circular |
| 7 | Dutch National Flag | 3-way partition |

---

## 📋 Problem Statements

### Problem 1 — Maximum Subarray Sum (Kadane's Algorithm)
> Given an integer array `nums`, find the contiguous subarray with the largest sum.
> `Input: [-2,1,-3,4,-1,2,1,-5,4]` → `Output: 6` (subarray: [4,-1,2,1])

### Problem 2 — Rotate Array by K Steps
> Rotate array to the right by `k` steps in-place.
> `Input: [1,2,3,4,5,6,7], k=3` → `Output: [5,6,7,1,2,3,4]`

### Problem 3 — Subarray Sum Equals K
> Count subarrays with sum exactly equal to k using prefix sum + hashmap.
> `Input: [1,1,1], k=2` → `Output: 2`

### Problem 4 — Maximum Sum of Fixed Window
> Find max sum of any contiguous subarray of size k.
> `Input: [2,1,5,1,3,2], k=3` → `Output: 9`

### Problem 5 — Trapping Rainwater
> Calculate total water trapped between bars.
> `Input: [0,1,0,2,1,0,1,3,2,1,2,1]` → `Output: 6`

---

## 💻 Solutions + Time & Space Complexity

```python
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
```

---

## ⏱️ Complexity Reference Table

| Algorithm | Time | Space | Notes |
|-----------|------|-------|-------|
| Kadane's | O(n) | O(1) | Single pass |
| Rotate (reversal) | O(n) | O(1) | In-place |
| Subarray Sum K | O(n) | O(n) | Prefix + HashMap |
| Fixed Window | O(n) | O(1) | Sliding |
| Trapping Rain | O(n) | O(1) | Two pointers |
| Prefix Sum | O(n) build / O(1) query | O(n) | Precompute |

---

## 📚 Learning Notes

### 🔑 Key Insights

1. **Kadane's Algorithm** — At each position, decide: start fresh or extend current subarray. `cur = max(x, cur+x)`
2. **Rotation Trick** — Reverse entire → Reverse first K → Reverse rest K. Zero extra space!
3. **Prefix Sum Pattern** — `sum(l,r) = prefix[r+1] - prefix[l]`. Build once, query O(1).
4. **Sliding Window** — Expand right, shrink left. Track window state incrementally, not recompute.
5. **Two Pointers** — Move inward from both ends when array is sorted or symmetric reasoning applies.

### 💡 When to Use What
- **Contiguous subarray** problem → Kadane or Sliding Window
- **Range sum query** multiple times → Prefix Sum
- **Sorted array + pair/triplet** → Two Pointers
- **Rotate/reverse in-place** → Reversal Algorithm

---

## 🎯 Top Interview Questions

1. What is the time complexity of Kadane's algorithm and why is it O(n)?
2. How do you handle all-negative arrays in Kadane's algorithm?
3. Explain the reversal trick for array rotation. Why does it work?
4. How does prefix sum enable O(1) range queries?
5. What's the difference between fixed and dynamic sliding windows?
6. When does the two-pointer approach work? What preconditions are needed?
7. How would you find the maximum sum circular subarray?
8. Explain Dutch National Flag algorithm and its time/space complexity.
9. How do you find all subarrays with sum = k? What data structure helps?
10. What is the minimum window subarray problem and how do you solve it?

---

## ⚠️ Edge Cases to Always Check

- Empty array `[]` — handle with guard clause
- All negative numbers — Kadane must still find max (not 0)
- Single element array — return that element
- k > n in rotation — use `k %= n`
- k = 0 or k = n in rotation — no change needed
- Overflow — use Python (no overflow) or long in Java/C++
- All same elements in subarray problems
- Array with zeros in subarray sum problems

---

## 🧪 Test Cases

```python
import pytest

def test_kadane():
    assert kadane([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert kadane([-1,-2,-3]) == -1          # all negative
    assert kadane([5]) == 5                   # single element
    assert kadane([1,2,3,4,5]) == 15          # all positive

def test_rotate():
    assert rotate_array([1,2,3,4,5,6,7],3) == [5,6,7,1,2,3,4]
    assert rotate_array([1,2],3) == [2,1]     # k > n

def test_subarray_sum():
    assert subarray_sum_k([1,1,1],2) == 2
    assert subarray_sum_k([1,2,3],3) == 2
    assert subarray_sum_k([1],0) == 0

def test_rain_water():
    assert trap_rain_water([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
    assert trap_rain_water([4,2,0,3,2,5]) == 9
    assert trap_rain_water([]) == 0 if not [] else True
```

---

## 📦 Project Structure

```
DSA-Arrays-Mastery/
├── solutions/
│   ├── main.py            ← All core solutions
│   ├── kadane.py          ← Kadane variants
│   ├── prefix_sum.py      ← Prefix sum problems
│   ├── sliding_window.py  ← Sliding window patterns
│   └── two_pointer.py     ← Two pointer problems
├── tests/
│   └── test_arrays.py     ← pytest test suite
├── notes/
│   └── complexity.md      ← Complexity cheat sheet
├── problems/
│   └── problem_list.md    ← 50 curated problems
└── README.md
```

---

## ⚡ Quick Start

```bash
# Clone
git clone https://github.com/kushagrabansal-IOT/DSA-Arrays-Mastery.git
cd DSA-Arrays-Mastery

# Run solutions
python solutions/main.py

# Run tests
python -m pytest tests/ -v
```

---

## 🚀 Future Improvements

- [ ] Add C++ implementations for all solutions
- [ ] Add Java implementations
- [ ] Visual diagrams for sliding window animation
- [ ] LeetCode problem links for each algorithm
- [ ] Add Segment Tree for range queries
- [ ] Add sparse table for static range min/max
- [ ] Add more DP on arrays problems
- [ ] Add interactive Python notebook (Jupyter)

---

## 📄 License

MIT License — Free to use, modify, distribute.

---

## 👨‍💻 Author

**Kushagra Bansal** — Founder @ Project Lab India, Jaipur
🔬 DSA • OOPS • DBMS • IoT • Competitive Programming
🏆 Innovation Award Recipient | IEEE Member
🛒 [radiomarket.in](https://radiomarket.in)

---

> ⭐ **Star this repo** if it helped your interview prep!
> 🍴 **Fork it** — add your own solutions!
> 📢 **Share it** — help other developers!
