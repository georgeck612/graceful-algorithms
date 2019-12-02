from Graph import Graph
from exhaustive_search import test_gracefulness

if __name__ == '__main__':
    graph = Graph([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
                  [(0, 1), (1, 2), (2, 3), (2, 4), (4, 5), (4, 6), (4, 7), (7, 8), (4, 9), (9, 10), (10, 11), (10, 12),
                   (10, 13), (13, 14)])
    test_gracefulness(graph)
