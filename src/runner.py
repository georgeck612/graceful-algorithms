from playsound import playsound

from src.Graph import Graph
from src.exhaustive_search import test_gracefulness

if __name__ == '__main__':
    # test of gracefulness on K_4
    k_5 = Graph([0,1,2,3,4,5,6],[(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(1,2),(1,3),(1,4),(1,5),(2,3),(2,4),(2,5),(3,4),(3,5),(4,5)])
   #  k_5 = Graph.generate_complete_graph(6)
   #  k_5.add_edge(0,6)
    is_graceful = test_gracefulness(k_5)
    print(k_5.graph)
    print(k_5.order)
    if is_graceful:
        playsound("res/tada.mp3")
    else:
        playsound("res/fail.mp3")
