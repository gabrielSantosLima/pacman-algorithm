from collections import deque

from graph import Graph, Vertex


def BFS(graph: Graph, origin: Vertex):
    discovered: dict[int, bool] = {}
    route: list[Vertex] = []

    for vertex in graph.vertices:
        discovered[vertex.ID] = False

    queue = deque()
    
    queue.append(origin)
    discovered[origin.ID] = True
    
    while queue:
        discovered_vertex: Vertex = queue.popleft()
        route.append(discovered_vertex)

        for i in discovered_vertex.vertices:
            if not discovered[i[0].ID]:
                discovered[i[0].ID] = True
                queue.append(i[0])

    return route