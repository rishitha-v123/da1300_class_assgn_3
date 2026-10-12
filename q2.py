from typing import List


def surviving_ships(ships: List[int]) -> List[int]:
    """
    Problem 2: Spaceship collisions.

    Given a list of ship engine powers (sign = direction: positive is
    right, negative is left), resolve all collisions between ships
    moving toward each other and return the engine powers (with sign)
    of the ships that remain.

    Args:
        ships: list of signed engine powers.

    Returns:
        List of signed engine powers of surviving ships, left to right.
    """
    stack_ =[]
    for ship in ships :
        a = True
        while stack_ and stack_[-1] > 0 and ship <0:
            if  abs(ship) > abs(stack_[-1]):
                stack_.pop()
            elif abs(ship) == abs(stack_[-1]):
                stack_.pop()
                a = False
                break
            else:
                a = False 
                break
        if a == True:
            stack_.append(ship)
    return stack_
 

if __name__ == "__main__":
    # Example sanity checks (see test.py for the real test cases)
    print(surviving_ships([6, 3, -5]))  # expected: [6]
    print(surviving_ships([8, -8]))     # expected: []
