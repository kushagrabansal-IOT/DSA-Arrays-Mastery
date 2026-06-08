# Learning Notes — DSA-Arrays-Mastery

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

## Complexity Reference

| Algorithm | Time | Space | Notes |
|-----------|------|-------|-------|
| Kadane's | O(n) | O(1) | Single pass |
| Rotate (reversal) | O(n) | O(1) | In-place |
| Subarray Sum K | O(n) | O(n) | Prefix + HashMap |
| Fixed Window | O(n) | O(1) | Sliding |
| Trapping Rain | O(n) | O(1) | Two pointers |
| Prefix Sum | O(n) build / O(1) query | O(n) | Precompute |