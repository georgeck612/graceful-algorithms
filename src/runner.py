from playsound import playsound

from src.Graph import Graph
from src.exhaustive_search import test_gracefulness, get_graceful_labelings_from_label_set, get_valid_label_sets, \
    get_representative_labels

if __name__ == '__main__':
    # test of gracefulness on the Petersen graph
    petersen_graph = Graph([0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                           [(0, 1), (0, 4), (0, 5), (1, 2), (1, 6), (2, 3), (2, 7), (3, 4), (3, 8), (4, 9), (5, 7),
                            (5, 8), (6, 8), (6, 9), (7, 9)])
