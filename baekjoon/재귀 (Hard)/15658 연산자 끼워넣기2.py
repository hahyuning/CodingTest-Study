def operation(index, sum, plus, minus, mul, div):
    if index == n:
        result.append(sum)
        return

    if plus > 0:
        operation(index + 1, sum + a[index], plus - 1, minus, mul, div)
    if minus > 0:
        operation(index + 1, sum - a[index], plus, minus - 1, mul, div)
    if mul > 0:
        operation(index + 1, sum * a[index], plus, minus, mul - 1, div)
    if div > 0:
        if sum >= 0:
            operation(index + 1, sum // a[index], plus, minus, mul, div - 1)
        else:
            operation(index + 1, -(-sum // a[index]), plus, minus, mul, div - 1)


n = int(input())
a = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

result = []
operation(1, a[0], plus, minus, mul, div)
print(max(result))
print(min(result))