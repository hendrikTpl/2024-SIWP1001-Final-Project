import unittest
from searching.depth_first import DepthFirst
class TestDFS(unittest.TestCase):
    def test_dfs(self):
        dfs = DepthFirst()
        graph = {1: [2, 3], 2: [4], 3: [4], 4: []}
        result = dfs.search(graph, 1)
        self.assertEqual(result, [1, 3, 4, 2])

if __name__ == "__main__":
    unittest.main()
