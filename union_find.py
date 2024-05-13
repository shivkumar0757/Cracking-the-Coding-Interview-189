# impelement union find for disjoint sets, using the optimised rank and updating parent

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)

        if rootP != rootQ:
            if self.rank[rootP] > self.rank[rootQ]:
                self.parent[rootQ] = rootP
            elif self.rank[rootP] < self.rank[rootQ]:
                self.parent[rootP] = rootQ
            else:
                self.parent[rootQ] = rootP
                self.rank[rootP] += 1

    def connected(self, p, q):
        return self.find(p) == self.find(q)           
    



# Test it
uf = UnionFind(10)
uf.union(1,2)
uf.union(5,6)
uf.union(2, 8)

print(uf.connected(1, 8))  #expected is True
print(uf.connected(5, 8))  #expected is Flase