import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

s = [0] * (n + 1)
for i in range(1, n + 1):
    s[i] = a[i - 1] + s[i - 1]

m = int(input())
for _ in range(m):
    start, end = map(int, input().split())
    print(s[end] - s[start - 1])
