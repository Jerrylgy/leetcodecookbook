class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #搜索问题，搜索空间是一个9*9的矩阵,因此递归的层级要有x,y两个坐标来表示
        #约束1，每一行中为1到9，所以确立一个9*9的rows矩阵，要求rows的每一行都独一无二
        #约束2，每一列中为1到9，所以确立一个9*9的cols矩阵，要求cols的每一行都独一无二
        #约束3，每一个9宫格里为1到9，所以确立一个3*3*9的matrix矩阵，要求matrx[0][0]到matrix[2][2]的每一行都独一无二
        #以上这个独一无二，可以采用就是类似n皇后中，append 检查in 然后pop的做法，也可以采用用bool值来表示，变为True,检查bool值，然后撤销为False的做法
        #考虑到list 的in 操作时间复杂度为n，比较慢，而集合操作起来又不是很方便pop和append，因此采取bool的方法
        #注意以下为初始化约束矩阵
        #注意这个space里存储的是真正的搜索空间中的点
        space = []
        rows = [[False for i in range(9)] for i in range(9)]
        cols = [[False for i in range(9)] for i in range(9)]
        matrix = [[[False for i in range(9)] for i in range(3)] for i in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    space.append([i,j])
                    continue
                else:
                    rows[i][int(board[i][j])-1] = True
                    cols[j][int(board[i][j])-1] = True
                    matrix[i//3][j//3][int(board[i][j])-1] = True
        n = len(space)
        print(n)
        #print(rows,cols,matrix)
        #这里关键就是要确立这个搜索空间，以及如何表示
        self.flag = False
        self.res = None
        #这里x，y代表了一个二维的矩阵搜索空间,board代表已搜索得结果，后面的三个形参就是约束
        #但是实际操作中，这样做对搜索空间的表达并不好，因为很多位置已经有数字了，实际上的搜索空间是那些没有数组的位置
        '''
        def backTrack(x,y,board,rows,cols,matrix):
            if x==9:
                self.res=board
                return
            
            for i in range(1,10):
                if rows[x][i-1] != True and cols[x][i-1] != True and matrix[x//3][y//3][i-1]!=True:
                    #做搜索选择
                    board[x][y] = str(i)
                    rows[x][i-1] = True
                    cols[x][i-1] = True
                    matrix[x//3][y//3][i-1] = True
                    #深一层级搜索（搜索空间中下一个位置的搜索）
                    if y<8:
                        backTrack(x,y+1,board,rows,cols,matrix)
                    elif y == 8:
                        backTrack(x+1,0,board,rows,cols,matrix)
                    #撤销搜索选择
                    board[x][y]="."
                    rows[x][i-1] = False
                    cols[x][i-1] = False
                    matrix[x//3][y//3][i-1] = False
                else:
                    continue
        backTrack(0,0,board,rows,cols,matrix)
        '''
        #这里可以不用把约束作为形参传进去，因为是原位修改True False
        #这里的pos用来在space空间中取点即可。
        def backTrack(pos):
            if pos==n:
                print(self.res)
                self.res=board
                self.flag = True
                return
            x,y = space[pos][0],space[pos][1]
            for i in range(1,10):
                if self.flag == True:
                    break
                if rows[x][i-1] != True and cols[y][i-1] != True and matrix[x//3][y//3][i-1]!=True:
                    #做搜索选择
                    board[x][y] = str(i)
                    rows[x][i-1] = True
                    cols[y][i-1] = True
                    matrix[x//3][y//3][i-1] = True
                    #深一层级搜索（搜索空间中下一个位置的搜索）
                    #print(board)
                    backTrack(pos+1)

                    #撤销搜索选择
                    #board[x][y]="."为什么不需要？
            
                    rows[x][i-1] = False
                    cols[y][i-1] = False
                    matrix[x//3][y//3][i-1] = False



        backTrack(0)
        return self.res
