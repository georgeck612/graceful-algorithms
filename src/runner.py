from playsound import playsound

from src.Graph import Graph
from src.exhaustive_search import test_gracefulness

if __name__ == '__main__':
    # test of gracefulness on the Petersen graph
    petersen_graph = Graph([0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                           [(0, 1), (0, 4), (0, 5), (1, 2), (1, 6), (2, 3), (2, 7), (3, 4), (3, 8), (4, 9), (5, 7),
                            (5, 8), (6, 8), (6, 9), (7, 9)])
    is_graceful = test_gracefulness(petersen_graph)
    if is_graceful:
        playsound("res/tada.mp3")
    else:
        playsound("res/fail.mp3")
