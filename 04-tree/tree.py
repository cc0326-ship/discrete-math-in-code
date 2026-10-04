from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def preorder(root):
    """前序：根 -> 左 -> 右"""
    if root is None:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)


def inorder(root):
    """中序：左 -> 根 -> 右"""
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


def postorder(root):
    """后序：左 -> 右 -> 根"""
    if root is None:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]


def levelorder(root):
    """层序：从上到下、从左到右（用队列，本质就是 BFS）"""
    if root is None:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


def height(root):
    """树的高度"""
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))


def insert_bst(root, val):
    """往二叉排序树插入一个值：小的往左，大的往右"""
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_bst(root.left, val)
    else:
        root.right = insert_bst(root.right, val)
    return root


def search_bst(root, val):
    """在二叉排序树里查找，返回（是否找到，比较了几次）"""
    steps = 0
    cur = root
    while cur:
        steps += 1
        if cur.val == val:
            return True, steps
        if val < cur.val:
            cur = cur.left
        else:
            cur = cur.right
    return False, steps


if 1:
    #         A
    #        / \
    #       B   C
    #      / \   \
    #     D   E   F
    a = TreeNode("A")
    b = TreeNode("B")
    c = TreeNode("C")
    d = TreeNode("D")
    e = TreeNode("E")
    f = TreeNode("F")
    a.left, a.right = b, c
    b.left, b.right = d, e
    c.right = f

    print("前序:", preorder(a))
    print("中序:", inorder(a))
    print("后序:", postorder(a))
    print("层序:", levelorder(a))
    print("树高:", height(a))

    print()

    nums = [50, 30, 70, 20, 40, 60, 80]
    bst = None
    for n in nums:
        bst = insert_bst(bst, n)

    print("插入顺序:", nums)
    print("BST 中序:", inorder(bst))
    print("BST 层序:", levelorder(bst))
    for key in [40, 65]:
        found, steps = search_bst(bst, key)
        print(f"查找 {key}: {'找到' if found else '不存在'}，比较 {steps} 次")
