import time
import locale
from math import factorial
from random import shuffle

locale.setlocale(locale.LC_ALL, 'en_US')


def is_graceful_labeling(graph, labeling):
    # initialize set of edge labels
    edge_labels = list(graph.edge_labels)

    # check if induced edge labeling is one-to-one
    for edge in graph.edges:
        u = edge[0]
        v = edge[1]
        if abs(labeling[u] - labeling[v]) in edge_labels:
            edge_labels.remove(abs(labeling[u] - labeling[v]))
        else:
            return False

    return True


def find_combinations(graph, iterable, r):
    labels_checked = 0
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    combo = tuple(pool[i] for i in indices)
    if 0 in combo and graph.size in combo:
        result = check_valid_permutations(graph, list(combo), len(combo))
        if result[0]:
            labels_checked += result[2]
            return result[0], result[1], labels_checked
        labels_checked += result[1]
    count = 0
    while True:
        count += 1
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return False, labels_checked
        indices[i] += 1
        for j in range(i + 1, r):
            indices[j] = indices[j - 1] + 1
        combo = tuple(pool[i] for i in indices)
        if 0 in combo and graph.size in combo:
            result = check_valid_permutations(graph, list(combo), len(combo))
            if result[0]:
                labels_checked += result[2]
                return result[0], result[1], labels_checked
            labels_checked += result[1]


def check_valid_permutations(graph, arr, n):
    labels_checked = 0

    c = []

    for i in range(0, n):
        c.append(0)

    if arr.index(graph.size) in graph.graph[arr.index(0)]:
        labels_checked += 1
        possible_labeling = format_labeling(arr)
        result = is_graceful_labeling(graph, possible_labeling)
        if result:
            return True, possible_labeling, labels_checked

    i = 0
    while i < n:
        if c[i] < i:
            if i & 1:
                arr[c[i]], arr[i] = arr[i], arr[c[i]]
            else:
                arr[0], arr[i] = arr[i], arr[0]

            if graph.graph[arr.index(0)] and (arr.index(graph.size) in graph.graph[arr.index(0)]):
                labels_checked += 1
                possible_labeling = format_labeling(arr)
                result = is_graceful_labeling(graph, possible_labeling)
                if result:
                    return True, possible_labeling, labels_checked
            c[i] += 1

            i = 0
        else:
            c[i] = 0
            i += 1

    return False, labels_checked


def format_labeling(labeling):
    result = {}
    for i in range(0, len(labeling)):
        result[i] = labeling[i]
    return result


def test_gracefulness(graph):
    if not graph.is_simple:
        print("Non-simple graphs are not graceful.")
        return False
    if graph.is_complete and graph.order > 4:
        print("Complete graphs are only graceful for order ≤ 4.")
        return False
    if graph.order > graph.size + 1:
        print("Insufficient edges to permit a graceful labeling")
        return False
    if graph.is_eulerian and ((graph.size - 1) % 4 is 0 or (graph.size - 2) % 4 is 0):
        print("Eulerian graphs with size m ≡ 1 or 2 (mod 4) are not graceful (Rosa, A. 1967).")
        return False

    total_labels = binomial(graph.size - 1, graph.order - 2) * (2 * graph.size) * factorial(graph.order - 2)
    print("Testing gracefulness (exhaustive search)... (" + str(
        locale.format("%d", total_labels, grouping=True)) + " possible labels to check)")
    start = time.time()

    vertex_labels = []
    for i in range(0, graph.size + 1):
        vertex_labels.append(i)

    labels_checked = 0

    result = find_combinations(graph, vertex_labels, graph.order)
    end = time.time()
    if result[0]:
        labels_checked += result[2]
        print("\nGraceful labeling found: " + str(format_labeling(result[1])) + "\nLabels checked: " + str(
            locale.format("%d", labels_checked, grouping=True)) + " (" + str(
            round(100 * labels_checked / total_labels, 2)) + "% of possible)" + "\nTime taken: " + str(
            locale.format("%d", round((end - start), 2), grouping=True)) + " seconds")
        return True
    labels_checked += result[1]

    print("\nNo graceful labeling found." + "\nLabels checked: " + str(
        locale.format("%d", labels_checked, grouping=True)) + " (" + str(
        round(100 * labels_checked / total_labels, 2)) + "% of possible)" + "\nTime taken: " + str(
        locale.format("%d", round((end - start), 2), grouping=True)) + " seconds")
    return False


def binomial(x, y):
    try:
        result = factorial(x) // factorial(y) // factorial(x - y)
    except ValueError:
        result = 0
    return result
