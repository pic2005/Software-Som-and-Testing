def caesarCipher(s, k):
    encrypted_text = ""
    k = k % 26  
    
    for char in s:
        if char.isalpha():  
            shift = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - shift + k) % 26 + shift)
        else:
            encrypted_text += char 
    
    return encrypted_text

# Test cases
test_cases = [
    ("middle-Outz", 2),  # Expected: "okffng-Qwvb"
    ("Hello-World!", 4),  # Expected: "Lipps-Asvph!"
    ("abcXYZ", 3),  # Expected: "defABC"
    ("12345", 5),  # Expected: "12345" (no change)
    ("xyz", 1),  # Expected: "yza"
    ("XYZ", 1),  # Expected: "YZA"
    ("aBcD", 26),  # Expected: "aBcD" (no change, k=26 is equivalent to k=0)
    ("aBcD", 0),  # Expected: "aBcD" (no change)
    ("aBcD", 27),  # Expected: "bCdE" (k=27 is equivalent to k=1)
    ("!@#$%", 10),  # Expected: "!@#$%" (no change)
    ("", 5),  # Expected: "" (empty string)
    ("som", 3),           # Expected: "vrp"
    ("songtis", 5),       # Expected: "xtslynx"
    ("6710110289", 10),   # Expected: "6710110289" (no change)
    ("LOve", 2),          # Expected: "NQxg"
]   

# Run test cases
for i, (s, k) in enumerate(test_cases):
    result = caesarCipher(s, k)
    print(f'Test Case {i + 1}:')
    print(f'Input: s = "{s}", k = {k}')
    print(f'Output: "{result}"')
    print()