from playsound import playsound

from src.Graph import Graph
from src.exhaustive_search import test_gracefulness

if __name__ == '__main__':
    # test of gracefulness on K_4
    is_graceful = test_gracefulness(Graph.generate_complete_graph(4))
    if is_graceful:
        playsound("res/tada.mp3")
    else:
        playsound("res/fail.mp3")
