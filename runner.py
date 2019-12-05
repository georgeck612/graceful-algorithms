from Graph import Graph
from exhaustive_search import test_gracefulness
from playsound import playsound

if __name__ == '__main__':
    # test of gracefulness on K_4
    is_graceful = test_gracefulness(Graph.generate_complete_graph(4))
    if is_graceful:
        playsound("res/tada.mp3")
    else:
        playsound("res/fail.mp3")
