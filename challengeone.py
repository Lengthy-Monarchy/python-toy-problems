def solution(A):
    N = len(A)
    moves = 0
    
    # Iterate through each box
    for i in range(N):
        diff = A[i] - 10  # Calculate the difference between current bricks and target (10)
        A[i] = 10  # Update current box with 10 bricks
        
        # Propagate the difference to neighboring boxes
        if diff > 0:  # If difference is positive, propagate to the next box
            j = i + 1
            while j < N and diff > 0:
                if A[j] < 10:  # Check if the next box has less than 10 bricks
                    # Move bricks from current box to next box
                    move_bricks = min(diff, 10 - A[j])
                    A[j] += move_bricks
                    diff -= move_bricks
                    moves += move_bricks
                j += 1
        elif diff < 0:  # If difference is negative, propagate to the previous box
            j = i - 1
            while j >= 0 and diff < 0:
                if A[j] > 10:  # Check if the previous box has more than 10 bricks
                    # Move bricks from previous box to current box
                    move_bricks = min(-diff, A[j] - 10)
                    A[j] -= move_bricks
                    diff += move_bricks
                    moves += move_bricks
                j -= 1
    
    # Check if all boxes have exactly 10 bricks
    for bricks in A:
        if bricks != 10:
            return -1
    
    return moves


