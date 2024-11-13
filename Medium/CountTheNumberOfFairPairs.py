class CountTheNumberOfFairPairs(object):

    def countFairPairs(self, nums, lower, upper):
        count = 0
        nums.sort()

        for i in range(len(nums) - 1):
            left, right = i, len(nums) - 1
            left_pivot, right_pivot = 1, 0
            is_left_pivot_init, is_right_pivot_init = False, False

            # Find right pivot
            while left < right:
                s = nums[left] + nums[right]
                if lower <= s <= upper:
                    right_pivot = right
                    is_right_pivot_init = True
                    break
                right -= 1

            right = left + 1

            # Find left pivot
            while right < right_pivot:
                s = nums[left] + nums[right]
                if lower <= s <= upper:
                    left_pivot = right
                    is_left_pivot_init = True
                    break
                right += 1

            # Update count
            if (is_right_pivot_init and not is_left_pivot_init) or (is_left_pivot_init and not is_right_pivot_init):
                count += 1
            else:
                count += (right_pivot - left_pivot + 1)

        return count
