# 가로 : M
# 세로 : N
# 높이 : H (층)

# 인접 : 상 하 좌 우 앞 뒤 (여섯방향)

# 토마토가 익는 최소일수 

from collections import deque




def bfs() :
  q = deque()
  v = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]

  cnt = 0
  for h in range(H) :
    for i in range(N) :
      for j in range(M) :
        if arr[h][i][j] == 1 : # 익은 토마토인 경우 
          q.append((h, i, j))  # 큐에 넣어주고
          v[h][i][j] = 1       # 방문처리
        
        elif arr[h][i][j] == 0 : # 안익은거면
          cnt += 1

  # 여기까지 하면, -1로 빈 곳과 안 익은 토마토가 있는 곳은 방문처리가 안되어있음, 익은 토마토의 좌표가 순서대로 큐에 들어가 있음 

  while q :
    # 이제 하나씩 큐에서 꺼내서 bfs를 진행해주면 됨 
    ch, ci, cj = q.popleft()

    for dh, di, dj in ((0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1), (-1, 0, 0), (1, 0, 0)) :
      nh, ni, nj = ch + dh, ci + di, cj + dj

      if 0 <= nh < H and 0 <= ni < N and 0 <= nj < M and arr[nh][ni][nj] == 0 and v[nh][ni][nj] == 0 :
        q.append((nh, ni, nj))
        v[nh][ni][nj] = v[ch][ci][cj] + 1
        cnt -= 1


  # 이제 큐에서 다 빠지고 나면 cnt 값에 따라서 결과를 출력한다. 
  
  if cnt == 0 : 
    return v[ch][ci][cj] -1
  else :
    return -1
  

  # ㅇㅇ





M, N, H = map(int, input().split())

arr = []



# 문제에서 2차원 배열로 입력을 주어줬으니까 2차원 배열로 받아야 함 !!
for _ in range(H):
    arr.append([list(map(int, input().split())) for _ in range(N)])

ans = bfs()
print(ans)













