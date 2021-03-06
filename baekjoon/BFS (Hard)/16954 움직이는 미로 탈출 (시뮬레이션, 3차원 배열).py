from collections import deque

a = [input() for _ in range(8)]

# 0초부터 8초까지 9개의 경우 체크
# check[i][j][k]: k초에 (i, j)에 있을 수 있는지의 여부
check = [[[False] * 9 for j in range(8)] for i in range(8)]
check[7][0][0] = True

q = deque()
q.append((7, 0, 0))

# ---------------------------------------------------------------------
dx = [0, 0, 1, -1, 1, -1, 1, -1, 0]
dy = [1, -1, 0, 0, 1, 1, -1, -1, 0]

ans = False
while q:
    x, y, t = q.popleft()
    # 위치에 도착한 경우
    if x == 0 and y == 7:
        ans = True
        break

    for k in range(9):
        nx, ny = x + dx[k], y + dy[k]
        # 시간이 8보다 커지는 경우에는 8로 설정 (8초 후에는 벽이 없기 때문에 맵 상태 변화 X)
        nt = min(t + 1, 8)
        if 0 <= nx < 8 and 0 <= ny < 8:
            # 이동하려는 곳의 t초 후의 지도가 벽인 경우
            if nx - t >= 0 and a[nx - t][ny] == '#':
                continue
            # 이동한 후에 벽이 내려오는 경우
            if nx - (t + 1) >= 0 and a[nx - t - 1][ny] == '#':
                continue

            # 그 외 경우
            if check[nx][ny][nt] == False:
                check[nx][ny][nt] = True
                q.append((nx, ny, nt))

print(1 if ans else 0)