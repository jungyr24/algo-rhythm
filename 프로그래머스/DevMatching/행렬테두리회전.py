def solution(rows, columns, queries):
    graph = [[columns*x + y for y in range(1, columns+1)] for x in range(rows)]

    answer = []

    for p in queries:
        x1, y1, x2, y2 = p
        x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
        stack = []
        tmp = graph[x1][y1]
        for x in range(x1, x2):
            stack.append(graph[x][y1])
            graph[x][y1] = graph[x+1][y1]

        for y in range(y1, y2):
            stack.append(graph[x2][y])
            graph[x2][y] = graph[x2][y+1]

        for x in range(x2, x1, -1):
            stack.append(graph[x][y2])
            graph[x][y2] = graph[x-1][y2]

        for y in range(y2, y1, -1):
            stack.append(graph[x1][y])
            graph[x1][y] = graph[x1][y-1] 

        graph[x1][y1+1] = tmp
        answer.append(min(stack))

    for i in range(rows):
        print(graph[i])
    
    print("min value: ", answer)

    

    return answer

solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]])
# print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
# print(solution((3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]])))
# print(solution((100, 97, [[1,1,100,97]])))