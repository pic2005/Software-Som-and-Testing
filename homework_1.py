def is_funny(s):
    s_diff = [abs(ord(s[i]) - ord(s[i - 1])) for i in range(1, len(s))]
    r_diff = s_diff[::-1]  # Reverse the ASCII difference list
    return "Funny" if s_diff == r_diff else "Not Funny"

def run_test_cases():
    # กำหนด test cases
    test_cases = [
        ("acxz", "Funny"),
        ("bcxz", "Not Funny"),
        ("aaaa", "Funny"),
        ("ab", "Funny"),
        ("abc", "Funny"),  # แก้ไขจาก "Not Funny" เป็น "Funny"
        ("a", "Funny"),
        ("", "Funny"),
        ("xyz", "Not Funny"),  
        ("xyzyx", "Funny"),  
        ("12321", "Funny"),  
        ("12345", "Not Funny"),  
        ("!@#$%", "Not Funny"),  
        ("!@#@!", "Funny"),  
        ("abcddcba", "Funny"),  
        ("abcdedcbaa", "Not Funny"),  
    ]

    # รัน test cases
    for i, (input_str, expected_output) in enumerate(test_cases):
        result = is_funny(input_str)
        print(f"Test Case {i + 1}: {input_str} -> {result} (Expected: {expected_output})")
        if result == expected_output:
            print("Passed")
        else:
            print("Failed")

if __name__ == '__main__':
    run_test_cases()