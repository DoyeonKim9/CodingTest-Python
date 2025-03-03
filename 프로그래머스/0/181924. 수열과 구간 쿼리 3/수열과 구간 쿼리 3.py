def solution(arr, queries):
    answer = arr
    for i in queries:
        arr[i[0]], arr[i[1]] = arr[i[1]], arr[i[0]]
    return answer