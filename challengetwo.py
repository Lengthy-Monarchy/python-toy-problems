def digit_sum(num):
    """Helper function to calculate the sum of digits for a given number."""
    return sum(map(int, str(num)))

def solution(A):
    # Dictionary to store the sum of digits for each number
    sum_dict = {}
    
    # Iterate through the array and populate the sum_dict
    for num in A:
        sum_digits = digit_sum(num)
        if sum_digits not in sum_dict:
            sum_dict[sum_digits] = []
        sum_dict[sum_digits].append(num)
    
    max_pair_sum = -1  # Initialize maximum pair sum
    
    # Iterate through the keys in sum_dict to find pairs with equal digit sums
    for key in sum_dict:
        if len(sum_dict[key]) > 1:  # Check if there are at least two numbers with the same digit sum
            pairs = sum_dict[key]
            # Find the maximum pair sum
            max_pair_sum = max(max_pair_sum, max(pairs) + min(pairs))
    
    return max_pair_sum if max_pair_sum != -1 else -1

