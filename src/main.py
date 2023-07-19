from bfs import BFS
from graph import Graph


def main():
    # TODO clear example after finish the final code of the game.
    graph = Graph(7)

    v1 = graph.add_vertex(0)
    v2 = graph.add_vertex(1)
    v3 = graph.add_vertex(2)
    v4 = graph.add_vertex(3)
    v5 = graph.add_vertex(30)
    v6 = graph.add_vertex(33)
    v7 = graph.add_vertex(34)

    graph.add_edge(v1, v2)
    graph.add_edge(v1, v3)
    graph.add_edge(v2, v4)
    graph.add_edge(v2, v5)
    graph.add_edge(v2, v6)
    graph.add_edge(v6, v7)

    graph.print_vertices()

    route = BFS(graph, v1)
    for vertex in route:
        print(f"{vertex.ID}")

main()