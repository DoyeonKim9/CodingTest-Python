def solution(a, d, included):
    answer = 0
    cnt = []
    
    for i in range(a, a + d * len(included), d):
        cnt.append(i)
        
    for j in range(len(included)):
        if included[j]:
            answer += cnt[j]
            
    return answer