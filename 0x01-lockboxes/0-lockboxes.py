#!/usr/bin/python3
"""
lockboxes algorithm
"""
from collections import deque


def canUnlockAll(boxes):
    """
    tries to unlock all box in boxes

    Args:
        boxes (list): box containing all boxes
    Return:
        True if all boxes are opened. Otherwise, False
    """
    if not boxes:
        return False

    n = len(boxes)
    visited = set()
    queue = deque([0])

    while queue:
        box = queue.popleft()
        visited.add(box)

        for key in boxes[box]:
            if key < n and key not in visited:
                queue.append(key)

    return len(visited) == n
