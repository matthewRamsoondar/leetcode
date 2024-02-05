def maxElement(n, maxSum, k):
    # we want to continue incrementing the value of
    # s[k] until we violate the maxSum

    def left_sum(j: int, n: int, k: int):
        if j >= k:
            return (2 * j * k - k**2 - k) // 2
        else:
            return ((j**2 - j) // 2) + k - j + 1

    def right_sum(j: int, n: int, k: int):
        if j >= n - k - 1:
            return (
                -2 * j + 2 * j * n - 2 * j * k - n**2 + 2 * n * k + n - k**2 - k
            ) // 2
        else:
            return ((j**2 - j) // 2) + n - k - j - 2

    j = 1

    while left_sum(j + 1, n, k) + j + 1 + right_sum(j + 1, n, k) <= maxSum:
        j += 1

    return j


# print(maxElement(3, 7, 1))
print(maxElement(445, 488, 0))


# test
