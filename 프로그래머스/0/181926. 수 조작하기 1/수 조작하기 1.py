def solution(n, control):
    cont = list(control)
    for i in range(len(cont)):
        if cont[i] == 'w':
            n += 1
        elif cont[i] == 's':
            n -= 1
        elif cont[i] == 'd':
            n += 10
        else:
            n -= 10
    answer = n
    return n