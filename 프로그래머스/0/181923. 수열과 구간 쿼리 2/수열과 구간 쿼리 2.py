def solution(arr, queries):
    answer = []
    
    for s, e, k in queries:
        lst = []
        for i in range(s, e+1):
            if arr[i] > k:
                lst.append(arr[i])
        if lst:
            answer.append(min(lst))
        else:
            answer.append(-1)
            
    
    return answer