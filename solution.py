class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        nums.sort()
        count = 0
        n = len(nums)
        
        for i in range(n-1):
            # 查找满足 lower <= nums[i] + nums[j] <= upper 的右边界
            left = self.binary_search_left(nums, i+1, n-1, lower - nums[i])
            right = self.binary_search_right(nums, i+1, n-1, upper - nums[i])
            
            if left <= right:
                count += right - left + 1
                
        return count
    
    def binary_search_left(self, nums, left, right, target):
        # 查找左边界
        l, r = left, right
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l
    
    def binary_search_right(self, nums, left, right, target):
        # 查找右边界
        l, r = left, right
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        return r

    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        if not answers:
            return 0
            
        # 使用字典统计每个回答的频次
        count = {}
        for answer in answers:
            count[answer] = count.get(answer, 0) + 1
        
        total = 0
        # 计算每个回答需要的最少兔子数
        for answer, frequency in count.items():
            group_size = answer + 1  # 每组能容纳的兔子数
            # 计算需要的完整组数（向上取整）
            groups = (frequency + group_size - 1) // group_size
            total += groups * group_size
            
        return total
