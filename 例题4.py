class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        #本质上可以看作是一个求一个n维的数组col（代表n行中棋子所在的列的索引），这个数组里的数的值为0~(n-1)，且互不相同（不能在同一列）
        #更进一步的，因为不能在同一斜线上，
        #维护一个lurd = [] 如果是从左上到右下的斜线,则colIndex - i not in lurd
        #维护一个rpld = [] 如果是从右上到左下的斜线,则colIndex + i not in rpld
        #因此本质上是求一个满足以上两个约束的n维向量搜索空间
        #采用回溯法
        self.res = []
        #同时，要用如下函数将这个n维的向量转换成题目所需要的答案的形式
        def trans(ls,ans):
            for i in range(n):
                row=""
                for j in range(n):
                    if j==ls[i]:
                        row+="Q"
                    else:
                        row+="."
                ans.append(row)

        
        temp = []
        lurd = []
        rpld = []
        def backTrack(i,temp,lurd,rpld):
            if i == n:
                ans = []
                trans(temp,ans)
                self.res.append(ans)
            for colIndex in range(n):
                #满足约束
                if colIndex not in temp and colIndex - i not in lurd and colIndex + i not in rpld:
                    #做搜索选择
                    temp.append(colIndex)
                    lurd.append(colIndex-i)
                    rpld.append(colIndex+i)
                    #深一层级搜索
                    backTrack(i+1,temp,lurd,rpld)
                    #撤销搜索选择
                    temp.pop()
                    lurd.pop()
                    rpld.pop()
                else:
                    #这一列不行就看下一列行不行
                    continue
        backTrack(0,temp,lurd,rpld)
        return self.res
