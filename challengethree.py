def solution(N):
    # Number of complete cycles of the alphabet
    complete_cycles = N // 26
    
    # Remaining letters after complete cycles
    remaining_letters = N % 26
    
    # Generate the string with complete cycles
    result = 'abcdefghijklmnopqrstuvwxyz' * complete_cycles
    
    # Append the remaining letters
    if remaining_letters > 0:
        result += 'abcdefghijklmnopqrstuvwxyz'[:remaining_letters]
    
    return result


