class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        self.res = []
        temp = []
        def backTrack(start,target,temp):
            if target == 0:
                self.res.append(temp[:])
                return 
            i = start
            while i<n:
                if candidates[i]<=target:
                    temp.append(candidates[i])
                    #和组合总和的母题不一样的地方之2就在于这个地方要从i+1开始进行下一个层级的搜索
                    #原因在于这个题目中规定每个数组在每个组合中只能使用一次
                    backTrack(i+1,target-candidates[i],temp)
                    temp.pop()
                    #和组合总和的母题不一样的地方之2就在于加了这一个剪枝的代码
                    #原因在于这个题目中，有重复的数字，而重复的数字会造成大量重复的组合，例如1 1 1 1 中找和为2的组合
                    #仔细思考这个地方的逻辑在于。这行代码位于temp中某个位置pop了之后。而一旦temp中某个位置元素被pop了之后，就代表了这个地方放这个元素的可能性已经被穷尽了。例如 1 1 1 1 中找和为2的组合，temp中[1,1]中第二个1被temp之后，就代表，这个位置上放1的可能性已经被穷尽，不需要冗杂的重复
                    while i+1 < n and candidates[i+1] == candidates[i]:
                        i+=1
                    i+=1
                else:
                    break
        backTrack(0,target,temp)
        return self.res