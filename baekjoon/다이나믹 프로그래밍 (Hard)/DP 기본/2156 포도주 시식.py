n = int(input())
w = [0] + [int(input()) for _ in range(n)]
# d[i] : w[i]까지 마셨을 때 마실 수 있는 포도주의 최대 양
# i를 안마시거나, i - 1을 안마시고 i를 마시거나, i - 2를 안마시고 i - 1, i를 마시는 경우의 최대값
# d[i] = max(d[i - 1], d[i - 2] + w[i], d[i - 3] + w[i - 1] + w[i])
d = [0] * (n + 1)
d[1] = w[1]

if n >= 2:
    d[2] = w[1] + w[2]
for i in range(3, n + 1):
    d[i] = max(d[i - 1], d[i - 2] + w[i], d[i - 3] + w[i - 1] + w[i])

print(d[n])