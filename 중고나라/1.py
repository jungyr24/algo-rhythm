from collections import deque
from typing import AnyStr

length = 0
def dfs(directory, current_dir, dirname, result):
    global length
    print("curr:", current_dir)
    result += dirname[current_dir-1]+'/'

    if len(directory[current_dir]) == 0:
        print("result:", result, len(result))
        if len(result) > length:
            length = len(result)
        print("len:", length)

    for i in directory[current_dir]:
        dfs(directory, i, dirname, result)
        
def solution(n, relation, dirname):
    if n == 1:
        return 4
    directory = [[] for _ in range(n+1)]

    for r in relation:
        s, e = r[0], r[1]
        directory[s].append(e)
    
    
    dfs(directory, 1, dirname, "")
    return length-1

# print(solution(7, [[1,2],[2,5],[2,6],[1,3],[1,4],[3,7]], ["root","abcd","cs","hello","etc","hello","solution"]))
# print(solution(7, [[1,2],[2,3],[3,4],[4,5],[1,6],[6,7]], ["root","a","b","c","d","efghij","k"]))
print(solution(1, [[1, 1]], ["root"]))