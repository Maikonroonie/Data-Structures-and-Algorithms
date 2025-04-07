class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

# getting all chest to queue and then bfs on that
        n=len(grid)
        m=len(grid[0])
        visited=set()
        inf=2**31 -1
        q=deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j]==0:
                    q.append((i, j))
        while q:
            i, j= q.popleft()
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                if 0<= i+dx <n and 0<= j+dy <m:
                    if grid[i+dx][j+dy]==inf:
                        grid[i+dx][j+dy] = grid[i][j] + 1
                        q.append((i+dx, j+dy))
                

                    

