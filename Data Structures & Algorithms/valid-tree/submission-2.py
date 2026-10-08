
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1:
            return False

        g = defaultdict(list)

        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        seen = set()

        def dfs(node, parent):
            seen.add(node)
            for nod in g[node]:
                if nod == parent:
                    continue

                if nod in seen:
                    return False

                if not dfs(nod, node):
                    return False
            return True

        if not dfs(0, -1):
            return False

        return len(seen) == n