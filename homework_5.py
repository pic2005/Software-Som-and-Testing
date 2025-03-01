def gridChallenge(grid):
    sorted_grid = ["".join(sorted(row)) for row in grid]

    n = len(sorted_grid)
    for col in range(len(sorted_grid[0])):
        for row in range(1, n):
            if sorted_grid[row][col] < sorted_grid[row - 1][col]:
                return "NO"
    
    return "YES"

test_cases = [
    (["abc", "ade", "efg"], "YES"),
    (["ebacd", "fghij", "olmkn", "trpqs", "xywuv"], "YES"),
    (["mpxz", "abcd", "wlmf"], "NO"),
    (["a"], "YES"),
    (["zyx", "wvu", "tsr"], "NO"),
    (["abcd", "efgh", "ijkl", "mnop"], "YES"),
    (["aaaa", "aaaa", "aaaa"], "YES")
]

# Run test cases
for grid, expected in test_cases:
    result = gridChallenge(grid)
    print(f"Input: {grid}")
    print(f"Expected: {expected}, Got: {result}")
    print("Test Passed:", result == expected)
    print("-" * 30)