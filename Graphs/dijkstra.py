#Dijkstra implementation using sets
adj = [
[(1,10),(2,15)],
[(0,10),(3,19)],
[(0,15),(3,17),(4,13)],
[(1,19),(2,17),(4,11)],
[(2,13),(3,11)]
]

infinity = 10**10

start = 0
end = 4
n = len(adj)
dist = n * [infinity]
pred = n * [None]
path = []

def dijkstra():

    dist[start] = 0

    q = set()
    q.add((start, 0))

    while q:
        v = q.pop()[0]

        for elem in adj[v]:
            u = elem[0] #adjacent node
            weight = elem[1] #weight asociated to that adjacent node

            if dist[v] + weight < dist[u]:
                q.discard((u, dist[u]))
                dist[u] = dist[v] + weight
                pred[u] = v
                q.add((u, dist[u]))

def restore_path():
    v = end
    while v != None:
        path.append(v)
        v = pred[v]
    path.reverse()

dijkstra()
restore_path()
print(pred)
print(dist)

print("The shortest path is:", path)
print("With a total weight of:", dist[end])


for i in range(len(path)-1):
    print(path[i],"->",path[i+1], "peso:", dist[path[i+1]]-dist[path[i]])