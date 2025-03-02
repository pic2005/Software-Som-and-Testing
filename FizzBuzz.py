def fizzbuzz(x):
    if x % 3 == 0 and x % 5 == 0:
        return "FizzBuzz"
    elif x % 3 == 0:
        return "Fizz"
    elif x % 5 == 0:
        return "Buzz"
    else:
        return str(x)

# Test cases
test_cases = [
    (3, "Fizz"),
    (5, "Buzz"),
    (15, "FizzBuzz"),
    (2, "2"),
    (9, "Fizz"),
    (10, "Buzz"),
    (30, "FizzBuzz"),
    (7, "7"),
    (67, "67"),
    (6710110289, "6710110289"),
    (289, "289"),
    (120705, "FizzBuzz"),
    (2548, "2548"),
    (999999999999, "Fizz"),
    (85864528452785, "Buzz")
]

# Run  test case 
for x, expected in test_cases:
    result = fizzbuzz(x)
    print(f"Input: {x}, Expected: {expected}, Got: {result}")