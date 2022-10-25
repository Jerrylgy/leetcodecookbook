class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        #升序排序，减小后续搜索的时间复杂度
        candidates.sort()
        self.res = [ ]
        n = len(candidates)
        temp = []
        def backTrack(i,target,temp):
            #返回到上一级递归层级
            if target==0:
                self.res.append(temp[:])
                return
            for i in range(i,n):
                if candidates[i]<=target:
                    temp.append(candidates[i])
                    backTrack(i,target-candidates[i],temp)
                    temp.pop()    
                else:
                    #该层次for循环终止，因为数组已经升序排序，如果当前i位置的元素大于target，后面的肯定也大于
                    #因此，需要做这样一个剪枝操作
                    break
        backTrack(0,target,temp)
        return self.res
