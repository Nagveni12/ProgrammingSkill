def has_pair_with_sum(arr, k):
    seen = set()
    for num in arr:
        if k - num in seen:
            return True
        seen.add(num)
    return False

# Test case
print(has_pair_with_sum([10, 15, 3, 7], 17))  # Output: True
