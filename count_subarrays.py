class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        left = curr_sum = count = 0
        
        for right in xrange(n):
            curr_sum += nums[right]
            while left <= right and curr_sum * (right - left + 1) >= k:
                curr_sum -= nums[left]
                left += 1
                
            if left <= right:
                count += right - left + 1
                
        return count

# 测试代码
def test_countSubarrays():
    solution = Solution()
    # 测试用例1
    nums1 = [2,1,4,3,5]
    k1 = 10
    print "Test case 1:", solution.countSubarrays(nums1, k1)  # 预期输出: 6
    
    # 测试用例2
    nums2 = [1,1,1]
    k2 = 5
    print "Test case 2:", solution.countSubarrays(nums2, k2)  # 预期输出: 5

if __name__ == "__main__":
    test_countSubarrays()
