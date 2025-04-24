class Solution(object):
    def countCompleteSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        distinct_total = len(set(nums))
        window = {}
        left = count = 0
        n = len(nums)

        for right in range(n):
            # Add current element to window
            window[nums[right]] = window.get(nums[right], 0) + 1
            
            # Try to minimize window while maintaining all distinct elements
            while len(window) == distinct_total:
                # All subarrays ending at right from current left are valid
                count += n - right
                
                # Remove leftmost element
                window[nums[left]] -= 1
                if window[nums[left]] == 0:
                    del window[nums[left]]
                left += 1
                
        return count
