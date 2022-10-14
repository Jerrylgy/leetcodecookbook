class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #以示例1为例子
        #整个矩阵的范围由lu(leftup,左上点)[0,0]和rd(rightdown,右下点)[4,4]圈定
        #在左上点所在的行进行二分搜索，左边界left 右边界right
        #只会有两种情况，如果找到target，返回True
        #找不到，那么整个矩阵中left以及left之后的列被全部排除（例如该例中l位于2这个索引位置，意味着2 3 4列的元素肯定都是大于target的，因为7这个元素已经比target大了。这里最终退出biSearch时，left的位置可能会有几种情况，自己试验一下就会发现这种规则都适用），lu点所在的行被排除（二分搜索没搜索到，自然排除）
        #接着，在左上点所在的列进行二分搜索，类似于上面的方法，对称的操作
        #经过这两次操作之后，得到了新的lu和rd点
        #直到lu和rd圈定的范围被缩小到为不可能后，退出大搜索的while
        m = len(matrix)
        n = len(matrix[0])
        lu,rd = [0,0],[m-1,n-1]
        self.res = False
        #该函数用来搜索某一行或者某一列的target
        #注意这个地方关键的就是确定搜索的左右边界
        def biSearch(l,r,arr):
            while l<=r:
                m = l + (r-l)//2
                if arr[m]<target:
                    l = m+1
                elif arr[m]>target:
                    r = m-1
                else:
                    self.res = True
                    break
            #这一步锁定答案位置也很重要，要自己画图理解为什么l和l之后的列（行）区域都被排除
            return l
        #在大的搜索中，退出条件的确定比较重要        
        while (lu[0]<=rd[0] and lu[1]<=rd[1]):
            #获得lu所在的行
            row = matrix[lu[0]]
            temp = biSearch(lu[1],rd[1],row)
            if self.res == True:
                return True
            lu[0] += 1
            rd[1] = temp-1
            #获得lu所在列
            col = [row[lu[1]] for row in matrix]
            temp = biSearch(lu[0],rd[0],col)
            if self.res == True:
                return True
            lu[1] += 1
            rd[0] = temp-1

            print(lu,rd)

        return self.res        
