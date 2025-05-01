class Solution(object):
    def maxTaskAssign(self, tasks, workers, pills, strength):
        """
        :type tasks: List[int]
        :type workers: List[int]
        :type pills: int
        :type strength: int
        :rtype: int
        """
        n = len(tasks)
        m = len(workers)
        tasks.sort()  # 任务按难度升序排序
        workers.sort()  # 工人按能力升序排序

        def check(count):
            if count > m:
                return False

            import bisect
            # 选择最弱的count个任务
            curr_tasks = tasks[:count]
            # 选择最强的count个工人
            curr_workers = workers[m - count:]
            remaining_pills = pills

            # 从最强的工人开始匹配
            for worker in curr_workers:
                if worker >= curr_tasks[0]:
                    # 不使用药丸能完成最简单的任务
                    idx = bisect.bisect_right(curr_tasks, worker)
                    curr_tasks.pop(idx - 1)
                elif remaining_pills > 0:
                    # 尝试使用药丸
                    new_ability = worker + strength
                    if new_ability >= curr_tasks[0]:
                        idx = bisect.bisect_right(curr_tasks, new_ability)
                        curr_tasks.pop(idx - 1)
                        remaining_pills -= 1
                    else:
                        return False
                else:
                    return False

            return len(curr_tasks) == 0

        # 二分查找最大可完成任务数
        left, right = 0, min(n, m) + 1
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid

        return left - 1


solution = Solution()
tasks = [5, 9, 8, 5, 9]
workers = [1, 6, 4, 2, 6]
pills = 1
strength = 5
print(solution.maxTaskAssign(tasks, workers, pills, strength))
    