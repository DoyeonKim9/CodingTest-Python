def solution(n):
    answer = []
    answer.append(n)
    for i in range(n):
        if n % 2 == 0:
            n /= 2
            answer.append(n)
        else:
            n = 3*n+1
            answer.append(n)
        if n == 1:
            break
    return answer