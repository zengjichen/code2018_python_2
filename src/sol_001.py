

'''


其中要注意每个initial中元素ini所在的联通分量我们还要去除它里面含有的本身就在initial中的其他元素，
因为对于这些元素，事实上即使我们删除了ini，也minimize不了它们。
所以要算一下每个initial里面的元素所在的联通分量里面包含的其他的initial元素的个数，代码中用dup表示

graph长度为N，

find()时间复杂度为O(N), union为O(1)，所以最终时间复杂度为O(len(graph)^2)

空间为O(N

'''

class Solution(object):
    def minMalwareSpread(self, graph, initial):
        """
        :type graph: List[List[int]]
        :type initial: List[int]
        :rtype: int
        """

        def find(x):
            while x != uf[x]:
                uf[x] = uf[uf[x]]
                x = uf[x]
            return uf[x]

        def union(x, y):
            x_root = find(x)
            y_root = find(y)
            uf[x_root] = y_root

        uf = [i for i in range(len(graph))]
        for i in range(len(graph)):
            for j in range(i + 1, len(graph)):
                if graph[i][j]:
                    union(i, j)  # 并查集
        lookup, dup = {}, {}
        for i in range(len(graph)):
            root = find(i)
            lookup[root] = lookup.get(root, 0) + 1  #Python 字典(Dictionary) get() 函数返回指定键的值，如果值不在字典中返回默认值
            if i in initial:  # 这里是算一下每个initial里面的元素所在的联通分量里面包含的其他的initial元素的个数
                dup[root] = dup.get(root, -1) + 1  # 这里默认值是-1就代表不把自己包含进去了，算的是所有其

        component_sizes_of_initial = [lookup[find(ini)] - dup[find(ini)] for ini in initial]
        max_component_size = max(component_sizes_of_initial)

        res = []
        for i in range(len(initial)):
            if component_sizes_of_initial[i] == max_component_size:
                res.append(initial[i])
        return min(res)
