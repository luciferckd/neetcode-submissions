class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        g = defaultdict(list)

        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        seen = set()
        def dfs(node):
            seen.add(node)
            for nod in g[node]:
                if nod not in seen:
                    dfs(nod)

        res = 0

        for i in range(n):
            if i not in seen:
                res += 1
                dfs(i)

        return res