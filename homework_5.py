def gridChallenge(grid):
    # Step 1: Sort each row
    sorted_grid = ["".join(sorted(row)) for row in grid]
    
    # Step 2: Check if columns are sorted
    n = len(sorted_grid)
    for col in range(len(sorted_grid[0])):
        for row in range(1, n):
            if sorted_grid[row][col] < sorted_grid[row - 1][col]:
                return "NO"
    
    return "YES"

# Test cases
test_cases = [
    [
        "1",
        "5",
        "eabcd",
        "fghij",
        "olkmn",
        "trpqs",
        "xywuv"
    ],  #
    # Test Case 1: สามารถจัดเรียงได้
    [
        "abc",
        "def",
        "ghi"
    ],  # Expected: "YES"

    # Test Case 2: ไม่สามารถจัดเรียงได้
    [
        "bac",
        "def",
        "ghi"
    ],  # Expected: "NO"

    # Test Case 3: สามารถจัดเรียงได้
    [
        "a",
        "b",
        "c"
    ],  # Expected: "YES"

    # Test Case 4: ไม่สามารถจัดเรียงได้
    [
        "zxy",
        "abc",
        "def"
    ],  # Expected: "NO"

    # Test Case 5: สามารถจัดเรียงได้
    [
        "abcd",
        "efgh",
        "ijkl",
        "mnop"
    ],  # Expected: "YES"

    # Test Case 6: ไม่สามารถจัดเรียงได้
    [
        "abcd",
        "efgh",
        "ijkl",
        "mnop",
        "qrst",
        "uvwx",
        "yzab"
    ],  # Expected: "NO"

    # Test Case 7: สตริงว่าง
    [
        ""
    ],  # Expected: "YES"

    # Test Case 8: เมทริกซ์ขนาด 1x1
    [
        "a"
    ],  # Expected: "YES"

    # Test Case 9: เมทริกซ์ขนาด 2x2
    [
        "ab",
        "cd"
    ],  # Expected: "YES"

    # Test Case 10: เมทริกซ์ขนาด 3x3
    [
        "abc",
        "ade",
        "afg"
    ],  # Expected: "YES"
]

# Run test cases
for i, grid in enumerate(test_cases):
    result = gridChallenge(grid)
    print(f'Test Case {i + 1}:')
    print(f'Input: {grid}')
    print(f'Output: {result}')
    print()