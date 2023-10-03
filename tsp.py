import sys

def tsp(graph, start):
    n = len(graph)
    memo = {}

    # Define a bitmask to keep track of visited nodes
    visited_all = (1 << n) - 1

    def dp(mask, current):
        if mask == visited_all:
            return graph[current][start]

        if (mask, current) in memo:
            return memo[(mask, current)]

        min_cost = sys.maxsize
        for city in range(n):
            if not (mask & (1 << city)):
                new_mask = mask | (1 << city)
                cost = graph[current][city] + dp(new_mask, city)
                min_cost = min(min_cost, cost)

        memo[(mask, current)] = min_cost
        return min_cost

    return dp(1 << start, start)

# Example usage
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
start_city = 0

min_cost = tsp(graph, start_city)
print(f"The minimum cost of visiting all cities starting from city {start_city} is:", min_cost)
