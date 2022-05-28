#Code by Pranav Sai

def check_min(l):
    n = len(l)
    i = n-2

    while i >= 0 and l[i] > l[i+1]:
        i -= 1
    
    if i == -1:
        return False

    j = i+1
    while j < n and l[j] > l[i]:
        j += 1

    j -= 1

    l[i], l[j] = l[j], l[i]
    left = i+1
    right = n-1

    while left < right:
        l[left], l[right] = l[right], l[left]
        left += 1
        right -= 1
    return True

















from sys import maxsize
def TSP(graph,start):
    v=[]
    points=len(graph)
    for i in range(points):
        if i!=start:
            v.append(i)
    print(v)
    min_path=maxsize
    
    while True:
        cost=0
        s=start
        for i in range(len(v)):
            cost+=graph[s][v[i]]
            s=v[i]
        cost += graph[s][start]
        min_path=min(min_path,cost)
        if not check_min(v):
            break
    return min_path

graph=[
    [0,7,3],
    [4,0,7],
    [3,8,0]
]
start=0
res=TSP(graph,start)
print("Total Cost of Shortest Path:",res)
