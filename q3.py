
from typing import Optional


class TreeNode:
    """Binary tree node for the org chart."""
    def __init__(self, salary=0, left=None, right=None):
        self.salary = salary
        self.left = left
        self.right = right


def count_fair_managers(root: Optional[TreeNode]) -> int:
    count = 0

    def find(node):
        nonlocal count

        if node is None:
            return 0, 0

        ls, ln = find(node.left)
        rs, rn = find(node.right)

        total = ls + rs + node.salary
        num = ln + rn + 1

        if node.salary == total // num:
            count += 1

        return total, num

    find(root)
    return count


if __name__ == "__main__":
    root = TreeNode(1)
    print(count_fair_managers(root))  # expected: 1
