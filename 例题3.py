class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #搜索问题，logn时间复杂，应用二叉搜索
        #这道题目的有趣就在于，告诉了我们，应用二叉搜索不一定需要是一个严格上有升序或降序的数据结构
        #以数组为例，只要该数组的数据有某种特征，让我们可以通过中点二分减小搜索范围的方式去搜索，就可以运用二叉查找法。

        #确定左右边界，这个题目中，-1位置和n位置的元素为负无穷，数组长度大于等于1，这就意味着数组中至少有一个山峰

        left , right = 0 , len(nums)-1
        
        #分几种情况，负无穷 1 2 3 负无穷，负无穷 3 2 1 负无穷，负无穷 3 1 2 负无穷，负无穷 1 3 2 负无穷，负无穷 2 3 1 负无穷，负无穷 2 1 3 负无穷
        #确定退出规则
        while left < right:
            mid = left + (right-left)//2
            print(left,right,mid)
            #确定边界缩小规则
            #注意这个地方的搜索范围也不是对称的，取决于是拿mid和mid+1比，还是mid和mid-1比，通过在上面划分的情况中实验一下就知道了
            if nums[mid]<nums[mid+1]:
                left = mid+1
            else:
                right = mid
        #锁定答案位置
        #最终取left位置，也是通过实验得知
        return left
