"""BFS profiling program for SLE-2: 1000-node graph, start 0, goal 999."""
from collections import deque
from timeit import repeat

N = 1000

def build_graph():
    graph = {i: [] for i in range(N)}
    for i in range(N - 1):
        graph[i].append(i + 1)
        graph[i + 1].append(i)
    for i in range(0, N - 2, 10):
        graph[i].append(i + 2)
        graph[i + 2].append(i)
    return graph

GRAPH = build_graph()

def bfs(start, goal, graph):
    queue = deque([start])
    visited = {start}
    parent = {start: None}
    expanded = 0

    while queue:
        node = queue.popleft()
        expanded += 1
        if node == goal:
            break
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                parent[neighbour] = node
                queue.append(neighbour)

    if goal not in visited:
        return [], expanded

    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = parent[node]
    return path[::-1], expanded

if __name__ == "__main__":
    start, goal = 0, 999
    path, expanded = bfs(start, goal, GRAPH)
    timings = repeat(lambda: bfs(start, goal, GRAPH), repeat=3, number=1)

    print("BFS - Breadth-First Search")
    print(f"Start Node     : {start}")
    print(f"Goal Node      : {goal}")
    print(f"Goal Found     : {bool(path)}")
    print(f"Nodes Expanded : {expanded}")
    print(f"Best Time (ms) : {min(timings) * 1000:.5f}")
    print(f"Worst Time(ms) : {max(timings) * 1000:.5f}")
    print(f"Average (ms)   : {(sum(timings) / len(timings)) * 1000:.5f}")
    print(f"Path Length    : {len(path)}")
