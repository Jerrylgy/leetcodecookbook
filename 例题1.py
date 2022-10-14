class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #这个就是二分查找的母题了
        #有序的数据机构，搜索问题，二分查找的范式
        #确定左右边界
        #很明显，我们要从整个整型数组中搜索
        left,right =  0,len(nums)-1
        #确定退出条件
        #也就是说，当left和right划定的搜索范围内仍然有合法的元素时,一直搜索
        while left<=right:
            #一个二分查找中常见的取中点方法，偏左的地板除。即 1 2 3 4中取到2这个元素 1 2 3 中取到2这个元素
            mid = left + (right-left)//2
            #确定左边边界缩小规则，每次缩小约一半，以达到logn的时间复杂度
            if nums[mid]<target:
                left = mid+1
            elif nums[mid]>target:
                right = mid-1
            else:
                #锁定答案位置
                return mid
        #退出搜索while后，自然意味着所有的可能性都已经被排除，因此返回False即可
        return -1
