class Solution(object):
    def preorderTraversal1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Iteratively
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return result

    def preorderTraversal(self, root):
        # Recursive
        self.result = []
        self.recur(root)
        return self.result

    def recur(self, node):
        if node:
            self.result.append(node.val)
            self.recur(node.left)
            self.recur(node.right)