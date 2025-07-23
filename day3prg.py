class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Serialize function
def serialize(root):
    if root is None:
        return "#,"
    return str(root.val) + "," + serialize(root.left) + serialize(root.right)

# Deserialize function
def deserialize(data):
    def helper(nodes):
        val = next(nodes)
        if val == "#":
            return None
        node = Node(val)
        node.left = helper(nodes)
        node.right = helper(nodes)
        return node
    
    node_list = iter(data.split(","))
    return helper(node_list)

node = Node('root',
            Node('left', Node('left.left')),
            Node('right'))

data = serialize(node)
print("Serialized:", data)

new_node = deserialize(data)
print("Deserialized:", new_node.left.left.val) 
