if __name__ == '__main__':
    # Problem
    # We need to create a binary tree.

    class TreeNode:
        def __init__(self,key):
            self.key = key
            self.left = None
            self.right = None

        def __repr__(self) -> str:
            return "Binary Tree <{}>".format(self.to_tuple())

        @staticmethod
        def parse_tuple(data):
            if isinstance(data, tuple) and len(data)==3:
                node = TreeNode(data[1])
                node.left = TreeNode.parse_tuple(data[0])
                node.right = TreeNode.parse_tuple(data[2])
            elif data is None:
                node = None
            else:
                node = TreeNode(data)  
            return node
        
        def to_tuple(self):
            if self is None:
                return None
            if self.left is None and self.right is None:
                return self.key
            return TreeNode.to_tuple(self.left), self.key, TreeNode.to_tuple(self.right)
    
        def traverse_in_order(self):
            if self is None:
                return []
            return TreeNode.traverse_in_order(self.left) + [self.key] + TreeNode.traverse_in_order(self.right)


        def traverse_pre_order(self):
            if self is None:
                return []
            return [self.key] + TreeNode.traverse_pre_order(self.left) + TreeNode.traverse_pre_order(self.right)


        def traverse_post_order(self):
            if self is None:
                return []
            return TreeNode.traverse_post_order(self.left) + TreeNode.traverse_post_order(self.right) + [self.key]

        def tree_height(self):
            if self is None:
                return 0
            return 1 + max(TreeNode.tree_height(self.left), TreeNode.tree_height(self.right))
        
        def tree_size(self):
            if self is None:
                return 0
            return 1 + TreeNode.tree_size(self.left) + TreeNode.tree_size(self.right)




    tree_tuple =((1,3,None),2,((None,3,4),5,(6,7,8)))
    tree = TreeNode.parse_tuple(tree_tuple)

    print(f'Root key: {tree.key}')
    print(f'Bottom right key: {tree.right.left.right.key}')

    print(f'Tuple tree: {TreeNode.to_tuple(tree)}')

    print("In-order traversal:", TreeNode.traverse_in_order(tree))
    print("Pre-order traversal:", TreeNode.traverse_pre_order(tree))
    print("Post-order traversal:", TreeNode.traverse_post_order(tree))

    print(f'tree height: {TreeNode.tree_height(tree)}')
    print(f'tree size: {TreeNode.tree_size(tree)}')