def floyd(dist, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

def display(dist, n):
    print("Shortest distance matrix:")
    for i in range(n):
        for j in range(n):
            if dist[i][j] == float('inf'):
                print("INF", end="\t")
            else:
                print(int(dist[i][j]), end="\t")
        print()

n = int(input("Enter number of vertices: "))

print("Enter adjacency matrix (use 'inf' for no edge):")
dist = []

for i in range(n):
    row = input().split()
    dist.append([
        float('inf') if x.lower() == 'inf' else int(x)
        for x in row
    ])

result = floyd(dist, n)
display(result, n)
