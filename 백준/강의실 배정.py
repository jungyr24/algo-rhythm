import heapq
import sys

N = int(input())
# lecture_room = []
# for i in range(n):
#     s, t = map(int, input().split())
#     lecture_room.append((s, t))

# lecture_room.sort(key=lambda x: x[0])

# q = []
# heapq.heappush(q, lecture_room[0][1])
timeTable = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
timeTable.sort(key=lambda x: x[0])

queue = []
heapq.heappush(queue,timeTable[0][1])


for i in range(1, N):
    start, end = timeTable[i]
    if queue[0] > start:
        heapq.heappush(queue, end)
    else:
        heapq.heappop(queue)
        heapq.heappush(queue, end)

print(len(queue))

"""
3
1 3
2 4
3 5
"""