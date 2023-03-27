from queue import PriorityQueue
from typing import Callable, List, TypeVar, Tuple


State = TypeVar('State')


def ucs(start: State, is_goal: Callable[[State], bool], expand: Callable[[State], List[Tuple[State, float]]]) -> State | None:
    """Lazy Uniform Cost Search.

    Args:
        start: start node
        is_goal: function to check if a node is the goal node
        expand: function to expand a node, returns a list of (child, cost) pairs

    Returns:
        The goal node when found. Returns None if no path is found.
        Some implementations off expand will not ever return None.
    """
    # is the start node the goal node?
    if is_goal(start):
        return start

    # start up the queue
    queue = PriorityQueue()
    queue.put((0, start))
    visited = set()

    while not queue.empty():
        cost, node = queue.get()
        visited.add(node)

        for child, child_cost in expand(node):
            # skip if already visited
            if child in visited:
                continue

            # check if it's goal
            if is_goal(child):
                return child

            # add to queue
            queue.put((cost + child_cost, child))

    return None
