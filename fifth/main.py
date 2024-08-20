import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def build_tree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.left = Node(8)
    root.left.left.right = Node(9)
    root.left.right.left = Node(10)
    root.left.right.right = Node(11)
    root.right.left.left = Node(12)
    root.right.left.right = Node(13)
    root.right.right.left = Node(14)
    root.right.right.right = Node(15)
    return root

def generate_color(step, total_steps):
    intensity = int(255 * (step / total_steps))
    return f'#{intensity:02x}{intensity:02x}{intensity:02x}'

def visualize_traversal(root, traversal_type):
    G = nx.Graph()
    pos = {}
    node_colors = {}
    edges = []

    def add_nodes_edges(node, x, y, level):
        if not node:
            return
        G.add_node(node.val)
        pos[node.val] = (x, -y)
        if node.left:
            G.add_edge(node.val, node.left.val)
            edges.append((node.val, node.left.val))
            add_nodes_edges(node.left, x - 1 / 2 ** level, y + 1, level + 1)
        if node.right:
            G.add_edge(node.val, node.right.val)
            edges.append((node.val, node.right.val))
            add_nodes_edges(node.right, x + 1 / 2 ** level, y + 1, level + 1)

    add_nodes_edges(root, 0, 0, 1)

    if traversal_type == 'DFS':
        stack = [root]
        visited = set()
        step = 0
        while stack:
            node = stack.pop()
            if node.val not in visited:
                visited.add(node.val)
                step += 1
                node_colors[node.val] = generate_color(step, len(G))
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
    elif traversal_type == 'BFS':
        queue = deque([root])
        visited = set()
        step = 0
        while queue:
            node = queue.popleft()
            if node.val not in visited:
                visited.add(node.val)
                step += 1
                node_colors[node.val] = generate_color(step, len(G))
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, node_color=[node_colors.get(node, '#ffffff') for node in G.nodes()],
            with_labels=True, arrows=False, node_size=2000)
    nx.draw_networkx_edges(G, pos, edgelist=edges, arrows=False)
    plt.title(f'{traversal_type} Traversal')
    plt.axis('off')
    plt.show()

tree_root = build_tree()
visualize_traversal(tree_root, 'DFS')
visualize_traversal(tree_root, 'BFS')