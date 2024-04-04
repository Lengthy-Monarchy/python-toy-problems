def solution(A):
    total_bricks = sum(A)
    N = len(A)

    if total_bricks != N * 10:
        return -1

    moves = 0
    current_sum = 0
    for i in range(N):
        target_sum = (i + 1) * 10
        current_sum += A[i]
        moves += abs(current_sum - target_sum)

    return moves
