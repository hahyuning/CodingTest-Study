import heapq

n, m = map(int, input().split())
a = list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
dist = [-1] * (n + 1)

for _ in range(m):
    aa, b, c = map(int, input().split())
    graph[aa].append((b, c))
    graph[b].append((aa, c))

q = []
heapq.heappush(q, (0, 0))
dist[0] = 0

while q:
    cost, now = heapq.heappop(q)
    if dist[now] != -1 and dist[now] < cost:
        continue

    for nxt, nxt_cost in graph[now]:
        nxt_cost += cost
        if nxt == n - 1 and (nxt_cost < dist[nxt] or dist[nxt] == -1):
            dist[nxt] = nxt_cost
            heapq.heappush(q, (nxt_cost, nxt))
        elif a[nxt] == 0 and (nxt_cost < dist[nxt] or dist[nxt] == -1):
            dist[nxt] = nxt_cost
            heapq.heappush(q, (nxt_cost, nxt))

print(dist[n - 1])
