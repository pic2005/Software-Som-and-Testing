import itertools

def is_alternating(s):
    """Check if the string consists of two alternating characters."""
    return all(s[i] != s[i + 1] for i in range(len(s) - 1))

def alternate(s):
    """Find the maximum length of a string that consists of only two alternating characters."""
    unique_chars = set(s)
    max_length = 0
    
    for char1, char2 in itertools.combinations(unique_chars, 2):
        filtered_s = [c for c in s if c in (char1, char2)]
        if is_alternating(filtered_s):
            max_length = max(max_length, len(filtered_s))
    
    return max_length

# Test cases
test_cases = [
    "beabeefeab",  # Expected: 5
    "abcabc",      # Expected: 6
    "aaaa",        # Expected: 0
    "ababab",      # Expected: 6
    "a",           # Expected: 0
    "",            # Expected: 0
    "abba",        # Expected: 2
    "121212",      # Expected: 6
    "1221",        # Expected: 2
    "xyzxyz",      # Expected: 6
    "som",         # Expected: 2
    "741085296385296",  # Expected: 4
    "pichaya",     # Expected: 3
    "eiei",        # Expected: 4
    "6710110",     # Expected: 2
]

# Run test cases
for i, s in enumerate(test_cases):
    result = alternate(s)
    print(f'Test Case {i + 1}:')
    print(f'Input: "{s}"')
    print(f'Output: {result}')
    print()