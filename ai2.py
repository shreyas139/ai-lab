from queue import PriorityQueue

def best_first_search(graph, start, target, heuristics):
    visited = set()
    pq = PriorityQueue()

    pq.put((heuristics[start], start, [start]))
    visited.add(start)

    while not pq.empty():
        h, node, path = pq.get()

        if node == target:
            return path, h

        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                visited.add(neighbour)
                pq.put((heuristics[neighbour], neighbour, path + [neighbour]))

    return None, None


# Example usage
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': [],
        'F': []
    }

    heuristics = {
        'A': 10,
        'B': 20,
        'C': 5,
        'D': 6,
        'E': 4,
        'F': 0
    }

    path, cost = best_first_search(graph, 'A', 'F', heuristics)
    print(f"path found by Best-first search: {path} with cost: {cost}")