from typing import List
from collections import deque

def printer_queue_order(pages: List[int]) -> List[int]:
    """
    Problem 1: Round-robin printer.

    Given the number of pages for each document (in submission order),
    simulate round-robin printing (one page at a time, front of queue
    to back of queue) and return the document indices in the order
    they finish printing.

    Args:
        pages: pages[i] is the number of pages in document i.

    Returns:
        List of document numbers in the order they finish printing.
    """
    n = len(pages)
    r_q = deque(n)
    f_r =[]
    while len(r_q)!= 0:
        i =  r_q.popleft()
        pages[i]-=1
        if pages[i] > 0:
            r_q.append(i)
        else:
            f_r.append(i)
    return f_r


if __name__ == "__main__":
    # Example sanity check (see test.py for the real test cases)
    print(printer_queue_order([1, 1, 1]))  # expected: [0, 1, 2]
