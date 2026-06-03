
def main():
    n , m = map(int, input().split())
    g = [[] for _ in range(n+1)]
    for _ in range(m):
        u , v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)

    whatEverFirstSearch(g,1,1)
    print()
    whatEverFirstSearch(g,1,0) 

def whatEverFirstSearch(g, u, flg):
    vis = set()
    sq = [u]
    while sq:
        if flg == 1: #bfs
            node = sq.pop(0)
        else: #dfs
            node = sq.pop()
        if node in vis:
            continue
        vis.add(node)
        print(node, end = " ")
        for v in g[node]:
            if v not in vis:
                sq.append(v)
        
main()