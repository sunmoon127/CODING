class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        """
        :type nums: List[int]
        :type minK: int
        :type maxK: int
        :rtype: int
        """
        result = 0
        last_min = last_max = invalid = -1
        
        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                invalid = i
            if num == minK:
                last_min = i
            if num == maxK:
                last_max = i
                
            if last_min >= 0 and last_max >= 0:
                valid_start = min(last_min, last_max)
                if valid_start > invalid:
                    result += valid_start - invalid
                    
        return result

# 测试代码
if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    nums1 = [1,3,5,2,7,5]
    minK1, maxK1 = 1, 5
    print("测试用例1结果: {}".format(solution.countSubarrays(nums1, minK1, maxK1)))  # 应输出2
    
    # 测试用例2
    nums2 = [1,1,1,1]
    minK2, maxK2 = 1, 1
    print("测试用例2结果: {}".format(solution.countSubarrays(nums2, minK2, maxK2)))  # 应输出10
