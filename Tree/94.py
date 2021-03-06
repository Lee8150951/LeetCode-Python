from treeNode import TreeNode
from treeNode import creatBTree
from typing import List
class Solution:
    # 迭代法
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

if __name__=="__main__":
    data = [1, 2, 2, 3, 2]
    root = creatBTree(data, 0)
    method = Solution()
    answer = method.inorderTraversal(root)
    print(answer)