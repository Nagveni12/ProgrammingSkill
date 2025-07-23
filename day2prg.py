def product_except_self(nums):
    n = len(nums)
    result = [1] * n

    # Left product pass
    left_product = 1
    for i in range(n):
        result[i] = left_product
        left_product *= nums[i]

    # Right product pass
    right_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]

    return result

# Example test cases
print(product_except_self([1, 2, 3, 4, 5]))   # Output: [120, 60, 40, 30, 24]
print(product_except_self([3, 2, 1]))         # Output: [2, 3, 6]
