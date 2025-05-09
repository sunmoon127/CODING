from collections import Counter, defaultdict
import numpy as np

MOD = 10**9 + 7

class Solution(object):
    def countBalancedPermutations(self, num):
        n = len(num)
        if n == 0:
            return 0
        
        # 预处理每个数字的出现次数
        counter = Counter(num)
        digits = [int(d) for d in sorted(counter.keys())]  # 将字符串转换为整数
        counts = [counter[str(d)] for d in digits]  # 使用字符串作为counter的键
        m = len(digits)
        
        # 计算奇数位和偶数位的数量
        odd_pos = (n + 1) // 2
        even_pos = n - odd_pos
        
        # 预处理阶乘和逆元
        maxn = n + 1
        fact = [1] * maxn
        inv_fact = [1] * maxn
        for i in range(1, maxn):
            fact[i] = fact[i-1] * i % MOD
        inv_fact[maxn-1] = pow(fact[maxn-1], MOD-2, MOD)
        for i in range(maxn-2, -1, -1):
            inv_fact[i] = inv_fact[i+1] * (i+1) % MOD
        
        def comb(a, b):
            """计算组合数C(a, b) mod MOD"""
            if a < 0 or b < 0 or a < b:
                return 0
            return fact[a] * inv_fact[b] % MOD * inv_fact[a - b] % MOD
        
        # 预计算所有可能用到的组合数
        comb_cache = {}
        for i in range(maxn):
            for j in range(i + 1):
                comb_cache[(i, j)] = fact[i] * inv_fact[j] % MOD * inv_fact[i - j] % MOD

        # 优化：使用defaultdict避免键检查
        dp = defaultdict(int)
        dp[(0, 0, 0)] = 1
        
        # 预计算每个位置能达到的最大和最小和
        max_sum = sum(max(digits) * min(odd_pos, counts[i]) for i in range(m))
        min_sum = sum(min(digits) * min(odd_pos, counts[i]) for i in range(m))
        
        # 计算所有数字的和
        total_sum = sum(val * cnt for val, cnt in zip(digits, counts))
        
        for i in range(m):
            d = digits[i]
            val = d  # 已经是整数了
            cnt = counts[i]
            
            new_dp = defaultdict(int)
            
            # 计算剩余可用的数字总数
            remaining_total = sum(counts[i:])
            
            for (ou, eu, s_odd), ways in dp.items():
                # 强化剪枝条件
                if ou > odd_pos or eu > even_pos:
                    continue
                
                remaining_positions = odd_pos + even_pos - ou - eu
                if remaining_positions > remaining_total:
                    continue
                
                # 剪枝：检查sum是否可能平衡
                curr_min = s_odd + min(digits[i:]) * (odd_pos - ou)
                curr_max = s_odd + max(digits[i:]) * (odd_pos - ou)
                target_sum = total_sum // 2
                if curr_max < target_sum or curr_min > target_sum:
                    continue

                max_k = min(cnt, odd_pos - ou)
                max_l = min(cnt, even_pos - eu)
                
                # 优化内层循环
                for k in range(max_k + 1):
                    remaining = cnt - k
                    if remaining < 0:
                        break
                        
                    for l in range(min(remaining + 1, max_l + 1)):
                        if k + l > cnt:
                            break
                            
                        new_ou = ou + k
                        new_eu = eu + l
                        new_s_odd = s_odd + k * val
                        
                        ways_comb = (comb_cache[(odd_pos - ou, k)] * 
                                   comb_cache[(even_pos - eu, l)]) % MOD
                        
                        new_dp[(new_ou, new_eu, new_s_odd)] = \
                            (new_dp[(new_ou, new_eu, new_s_odd)] + ways * ways_comb) % MOD
            
            # 过滤掉不可能的状态
            dp = {k: v for k, v in new_dp.items() 
                  if v != 0 and k[0] <= odd_pos and k[1] <= even_pos}
        
        # 计算结果：通过total_sum计算s_even
        total = 0
        for (ou, eu, s_odd), ways in dp.items():
            if ou == odd_pos and eu == even_pos:
                s_even = total_sum - s_odd
                if s_odd == s_even:
                    total = (total + ways) % MOD
        
        return total

# 测试目标用例
if __name__ == "__main__":
    sol = Solution()
    print(sol.countBalancedPermutations("139126774921041671742414033595624362657540238343404863487299285224099554785312776830473778173895"))  # 输出: 799669930