class Solution:
    def findMin(self, nums: List[int]) -> int:
        #排序数组，搜索问题，应用二分查找
        n = len(nums)
        #初始搜索范围的左右边界
        left,right = 0,n-1
        #制定搜索规则
        
        

        #这里最关键的就是制定这个搜索规则来减小搜索范围
        #关键就是先要列举出可能的有的情况，用具体的例子来化抽象为具象可能有 1 2 3 ， 3 1 2， 2 3 1
        #可以发现情况1和3，其l元素均大于m元素，但是其最小值所在方向却不同（一个需要r-1，一个需要l+1），因此如果比较m和l，就需要进一步细分讨论，比较繁琐
        #但是如果比较r元素和m元素，情况1和2，都是r元素>m元素，所需的操作都是r=m-1，情况3中r元素<m元素，需要的是l=m+1
        #这里的退出条件没有等号，是因为left和right的闭区间是锁定了答案的，一旦重合，说明找到了答案
        while left < right:            
            mid = left + (right-left)//2
            
            if nums[right]<nums[mid]:
                #这个地方的可以确保更新之后，left和right的闭区间一定可以锁住目标
                left = mid +1
            else:
                #注意，这个题目的搜索范围的减小是“不对称”的
                #如果这个地方right = mid -1的话，就无法保证left和right的闭区间可以锁住答案了。
                right = mid

        return nums[left]