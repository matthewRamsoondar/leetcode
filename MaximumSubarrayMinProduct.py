class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        res = 0
        prefix = [0]

        for num in nums:
            # the new prefix would be the previous prefix + the value of the current
            # element, because it starts at 0 we can just append
            prefix.append(prefix[-1] + num)

        # now track the current windows where each element in the stack
        # is going to be (start, min-val)
        stack = []
        i = 0
        while i < len(nums):
            # before we can add this element, we need to know
            # if it can overwrite and previous min subarrays
            start, num = i, nums[i]
            while stack and stack[-1][1] > num:
                # this value needs to get popped
                prev_start, prev_num = stack.pop()
                # compute the min-prod for this subarray
                min_prod = prev_num * (prefix[i] - prefix[prev_start])
                res = max(min_prod, res)
                start = prev_start

            stack.append((start, num))
            i += 1

        # for each value remaining in the stack we compute the min-product
        for start, min_val in stack:
            min_prod = min_val * (prefix[len(nums)] - prefix[start])
            res = max(min_prod, res)

        return res % ((10**9) + 7)
