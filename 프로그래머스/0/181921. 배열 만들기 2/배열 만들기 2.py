def solution(l, r):
    answer = []
    for i in range(l, r+1):
        check = True
        for s in str(i):
            if s != '0' and s !='5':
                check = False
                break
        if check == True:
            answer.append(i)
    if not answer:
        answer.append(-1)
    return answer