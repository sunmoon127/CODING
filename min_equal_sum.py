class Solution(object):
    def minSum(self, nums1, nums2):
        """计算使两个数组相等的最小和
        
        Args:
            nums1: List[int], 第一个数组
            nums2: List[int], 第二个数组
            
        Returns:
            long: 最小相等和，如果无法使两数组相等则返回-1
        """
        # 计算两个数组的当前和以及0的个数
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        zeros1 = nums1.count(0)
        zeros2 = nums2.count(0)
        
        # 如果一个数组没有0，而它的和小于另一个数组，则无解
        if (zeros1 == 0 and sum1 < sum2 + zeros2) or (zeros2 == 0 and sum2 < sum1 + zeros1):
            return long(-1)
            
        # 得到两个数组填充1后的最小和
        min_sum1 = sum1 + zeros1
        min_sum2 = sum2 + zeros2
        
        # 返回两个最小和中的较大者，转换为long类型
        return long(max(min_sum1, min_sum2))

# 测试代码
if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    nums1 = [3,2,0,1,0]
    nums2 = [6,5,0]
    print(solution.minSum(nums1, nums2))  # 应输出 12
    
    # 测试用例2
    nums1 = [2,0,2,0]
    nums2 = [1,4]
    print(solution.minSum(nums1, nums2))  # 应输出 -1
