def solution(array, commands):
    answer = []
    for start, end, k in commands:
        answer.append(sorted(array[start - 1: end])[k - 1])
    return answer


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
