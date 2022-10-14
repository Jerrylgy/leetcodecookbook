class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #基本思路就是转换
        #将一维数组里面的索引转换成这个矩阵里面的位置即可。
        #转换函数，将一维数组里的索引转换成二维矩阵中的索引即可。
        def convert(i,n):
            x,y = divmod(i,n)[0],divmod(i,n)[1]
            return [x,y]

        m = len(matrix)
        n = len(matrix[0])
        #确定左右边界
        left, right = 0, m*n-1
        #确定退出条件，注意这个地方退出后，left和right的关系可能错位，需要分情况讨论
        while left<right:
            mid = left + (right-left)//2
            x1,y1 = convert(mid,n)[0],convert(mid,n)[1]
            print(x1,y1)
            x2,y2 = convert(right,n)[0],convert(right,n)[1]
            #确定边界缩小规则
            if matrix[x1][y1]<target:
                left = mid+1
            elif matrix[x1][y1]>target:
                right = mid-1
            else:
                #锁定答案位置
                return True
    
        #锁定答案位置
        mid = left + (right-left)//2
        x1,y1 = convert(mid,n)[0],convert(mid,n)[1]
        if left == right:
            return True if matrix[x1][y1] == target else False
        return False 
