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

        for vertex in discovered_vertex.vertices:
            if not discovered[vertex.ID]:
                discovered[vertex.ID] = True
                queue.append(vertex)

    return route