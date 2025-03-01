def alternatingCharacters(s):
    deletions = 0
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            deletions += 1
    return deletions

# Test cases
test_cases = [
    "5",           # 0 (ไม่มีตัวอักษรซ้ำกันติดกัน)
    "AAAA",       # 3
    "BBBBB",      # 4
    "ABABABAB",   # 0
    "BABABA",     # 0
    "AAABBB",     # 4
    "ZZZZZZ",     # 5
    "AABBAABB",   # 4
    "ABCABC",     # 0
    "112233",     # 3
    "111222",     # 4
    "som",        # 0
    "pichaya",    # 0
    "120705",     # 0
    "aie",        # 0
    "8269841284269842658",  # 3
]

# Run test cases
for s in test_cases:
    result = alternatingCharacters(s)
    print(f'Input: "{s}" -> Output: {result}')