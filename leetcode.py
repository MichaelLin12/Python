class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [[''] * n for i in range(n)]
        return self.dfs(board, n, 0)

    def dfs(self, board, n, ans):
        print(n, ans)
        if n == 0:
            print(board)
            return 1  
        for i in range(len(board)):
            board[n-1][i] = 'Q'
            print('inter', board , i)
            if(self.isValid(board, i, n-1)):
                ans += self.dfs(board, n-1, 0)
                print('Out of stack', ans)
            board[n-1][i] = ''
    
        return ans
    
    def isValid(self, board, col, row):
        n = len(board)
        for i in range(n):
            if board[i][col] == 'Q' and i != row:
                return False
            if board[row][i] == 'Q' and i != col:
                return False
        
        i = 1
        while row + i < n and col + i < n:
            if board[row + i][col + i] == 'Q':
                return False
            i+=1
        
        i = 1
        while row - i >= 0 and col + i < n:
            if board[row - i][col + i] == 'Q':
                return False
            i+=1
        
        i = 1
        while row - i >= 0 and col - i >= 0:
            if board[row - i][col - i] == 'Q':
                return False
            i+=1

        i = 1
        while row + i < n and col - i >= 0:
            if board[row + i][col - i] == 'Q':
                return False
            i+=1
        
        return True




if __name__ == "__main__":
    s = Solution()
    print(s.totalNQueens(4))