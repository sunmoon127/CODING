class Solution:
    def countInterestingSubarrays(self, nums, modulo, k):
        n = len(nums)
        # 构建前缀和数组，prefix[i]表示前i个元素中满足条件的元素个数
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + (1 if nums[i] % modulo == k else 0)
        
        count = 0
        # freq[x]表示前缀和模modulo等于x的个数
        freq = {0: 1}
        
        # 遍历前缀和数组
        for i in range(1, n + 1):
            # 当前前缀和模modulo的值
            curr = prefix[i] % modulo
            # 寻找合适的之前的前缀和，使得区间满足条件
            target = (curr - k + modulo) % modulo
            count += freq.get(target, 0)
            # 更新频率表
            freq[curr] = freq.get(curr, 0) + 1
            
        return count

# 测试代码
if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    nums1 = [3, 2, 4]
    modulo1 = 2
    k1 = 1
    print(solution.countInterestingSubarrays(nums1, modulo1, k1))  # 输出: 3
    
    # 测试用例2
    nums2 = [3, 1, 9, 6]
    modulo2 = 3
    k2 = 0
    print(solution.countInterestingSubarrays(nums2, modulo2, k2))  # 输出: 2
