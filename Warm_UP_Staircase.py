def staircase(n, display="#"):
    if n <= 0 or n > 30:
        raise ValueError("n must be between 1 and 30")
    
    result = []
    for i in range(1, n + 1):
        # เพิ่มช่องว่างด้านหน้าเพื่อจัดรูปแบบบันได
        spaces = " " * (n - i)
        steps = display * i
        result.append(spaces + steps)
    return "\n".join(result)

def test_staircase():
    # Test Case 1
    n = 4
    display = "#"
    expected_output = "   #\n  ##\n ###\n####"
    
    result = staircase(n, display)
    
    assert result == expected_output, f"Test failed for n={n}, display='{display}'"
    print(f"Test Case 1 Passed! Output:\n{result}")

    # Test Case 2
    n = 3
    display = "*"
    expected_output = "  *\n **\n***"
    
    result = staircase(n, display)
 
    assert result == expected_output, f"Test failed for n={n}, display='{display}'"
    print(f"Test Case 2 Passed! Output:\n{result}")

    # Test Case 3
    n = 5
    display = "A"
    expected_output = "    A\n   AA\n  AAA\n AAAA\nAAAAA"
    
    result = staircase(n, display)
    
    assert result == expected_output, f"Test failed for n={n}, display='{display}'"
    print(f"Test Case 3 Passed! Output:\n{result}")

    # Test Case 4
    n = 1
    display = "#"
    expected_output = "#"
    
    result = staircase(n, display)

    assert result == expected_output, f"Test failed for n={n}, display='{display}'"
    print(f"Test Case 4 Passed! Output:\n{result}")

    # Test Case 5
    n = 30
    display = "#"
    expected_output = (
        "                             #\n"
        "                            ##\n"
        "                           ###\n"
        "                          ####\n"
        "                         #####\n"
        "                        ######\n"
        "                       #######\n"
        "                      ########\n"
        "                     #########\n"
        "                    ##########\n"
        "                   ###########\n"
        "                  ############\n"
        "                 #############\n"
        "                ##############\n"
        "               ###############\n"
        "              ################\n"
        "             #################\n"
        "            ##################\n"
        "           ###################\n"
        "          ####################\n"
        "         #####################\n"
        "        ######################\n"
        "       #######################\n"
        "      ########################\n"
        "     #########################\n"
        "    ##########################\n"
        "   ###########################\n"
        "  ############################\n"
        " #############################\n"
        "##############################"
    )
    
    result = staircase(n, display)
    
    assert result == expected_output, f"Test failed for n={n}, display='{display}'"
    print(f"Test Case 5 Passed! Output:\n{result}")

    # Test Case 6
    n = 6
    display = "@"
    expected_output = "     @\n    @@\n   @@@\n  @@@@\n @@@@@\n@@@@@@"
    
    result = staircase(n, display)
    
    assert result == expected_output, f"Test failed for n={n}, display='{display}'"
    print(f"Test Case 6 Passed! Output:\n{result}")

    # Test Case 7
    n = 10
    display = "289"
    expected_output = (
        "         289\n"
        "        289289\n"
        "       289289289\n"
        "      289289289289\n"
        "     289289289289289\n"
        "    289289289289289289\n"
        "   289289289289289289289\n"
        "  289289289289289289289289\n"
        " 289289289289289289289289289\n"
        "289289289289289289289289289289"
    )
    
    result = staircase(n, display)
    
    assert result == expected_output, f"Test failed for n={n}, display='{display}'"
    print(f"Test Case 7 Passed! Output:\n{result}")

    # Test Case 8
    n = 2
    display = "😊"
    expected_output = " 😊\n😊😊"

    result = staircase(n, display)
  
    assert result == expected_output, f"Test failed for n={n}, display='{display}'"
    print(f"Test Case 8 Passed! Output:\n{result}")

    # Test Case 9
    n = 0
    display = "#"
    try:
        result = staircase(n, display)
        assert False, "Expected ValueError but no exception was raised"
    except ValueError as e:
        assert str(e) == "n must be between 1 and 30", f"Unexpected error message: {e}"
        print(f"Test Case 9 Passed! Expected ValueError was raised.")

  
    # Test Case 10
    n = 5
    display = "6710110289"
    expected_output = (
        "    6710110289\n"
        "   67101102896710110289\n"
        "  671011028967101102896710110289\n"
        " 6710110289671011028967101102896710110289\n"
       "67101102896710110289671011028967101102896710110289"
)

    result = staircase(n, display)

    assert result == expected_output, f"Test failed for n={n}, display='{display}'"
    print(f"Test Case 11 Passed! Output:\n{result}")


# Run Test Cases
if __name__ == "__main__":
    test_staircase()