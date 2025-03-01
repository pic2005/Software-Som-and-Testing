def is_funny(s):
    # Calculate the absolute differences between consecutive characters
    s_diff = [abs(ord(s[i]) - ord(s[i - 1])) for i in range(1, len(s))]
    # Reverse the differences list
    r_diff = s_diff[::-1]
    # Check if the differences list is equal to its reverse
    return "Funny" if s_diff == r_diff else "Not Funny"

# Test cases
test_cases = [
    "abcba",          # Funny
    "abz",            # Not Funny
    "",               # Funny (empty string)
    "a",              # Funny (single character)
    "๑๒๓",            # Funny (Thai numerals)
    "a1B2",           # Not Funny
    "madam",          # Funny
    "abcdefgfedcba",  # Funny
    "a b c",          # Not Funny
    "!@#$%^&*()",     # Not Funny
]

# Run test cases and count results
funny_count = 0
not_funny_count = 0

for test in test_cases:
    result = is_funny(test)
    print(f'Input: "{test}" -> Output: {result}')
    if result == "Funny":
        funny_count += 1
    else:
        not_funny_count += 1

# Calculate percentages
total_cases = len(test_cases)
funny_percentage = (funny_count / total_cases) * 100
not_funny_percentage = (not_funny_count / total_cases) * 100

# Display percentages
print("\nResults Summary:")
print(f'Funny: {funny_percentage:.2f}%')
print(f'Not Funny: {not_funny_percentage:.2f}%')