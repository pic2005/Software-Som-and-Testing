def alternatingCharacters(s):
    deletions = 0
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            deletions += 1
    return deletions

def run_test_cases():
    # กำหนด test cases
    test_cases = [
        ("AAAA", 3),        # ลบ A 3 ตัว
        ("ABABAB", 0),      # ไม่ต้องลบอะไรเลย
        ("AABBB", 3),       # ลบ A 1 ตัวและ B 2 ตัว
        ("AAABBB", 4),      # ลบ A 2 ตัวและ B 2 ตัว
        ("", 0),           # สตริงว่าง
        ("A", 0),          # สตริงมีตัวอักษรเดียว
        ("AB", 0),         # สตริงไม่มีตัวอักษรซ้ำ
        ("AABB", 2),       # ลบ A 1 ตัวและ B 1 ตัว
        ("ABBA", 1),       # ลบ B 1 ตัว
        ("ABCDE", 0),      # ไม่ต้องลบอะไรเลย
        ("ABBCCCDDDDEEEEE", 10),  # ลบ B 1 ตัว, C 2 ตัว, D 3 ตัว, E 4 ตัว
    ]

    # รัน test cases
    for i, (input_str, expected_output) in enumerate(test_cases):
        result = alternatingCharacters(input_str)
        print(f"Test Case {i + 1}: {input_str} -> {result} (Expected: {expected_output})")
        if result == expected_output:
            print("Passed")
        else:
            print("Failed")

if __name__ == '__main__':
    run_test_cases()