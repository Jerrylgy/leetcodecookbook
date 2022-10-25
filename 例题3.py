class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        #这个数组就是搜索空间
        candidates = [i for i in range(1,10)]
        #我们要获得得满足条件的子搜索空间
        self.res = []
        temp = []
        
        def backTrace(index,count,target,temp):
            
            #通前两道题的区别在于这个地方多了一个约束，那么就在这个地方表达出来即可。
            #达到约束条件就要结束搜索
            if count == k:
                if target == 0:
                    self.res.append(temp[:])
                return 
            for i in range(index,9):
                #若满足搜索选择的条件
                if candidates[i]<=target:
                    #做搜索选择
                    temp.append(candidates[i])
                    backTrace(i+1,count+1,target-candidates[i],temp)
                    #撤销搜索选择
                    temp.pop()
                #剪枝
                else:
                    break
        backTrack(0,0,n,temp)
        return self.res
