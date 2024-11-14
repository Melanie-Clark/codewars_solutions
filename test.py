"""
HANDSHAKE CHALLENGE

You will need to:
- Write a function that takes an integer for the number of people and returns an integer with the number of handshakes
- Validate if a handshake can occur given X as an input
- Identify an error state and throw a custom exception
- Create a test file for the function and create a comprehensive test suite

"""
class NegativeValue(Exception):     # Exception to cover all exceptions
    """Raised for negative value inputs"""
    pass

class InvalidInput(Exception):     # Exception to cover all exceptions
    """Raised for invalid inputs"""
    pass

def no_of_handshakes(no_people: int) -> int:
    # initial tests if not an integer, as you can't have half people or negative people!
    if type(no_people) is not int:
        raise InvalidInput("Invalid input. Value must be a positive integer")
    elif no_people < 0:
        raise NegativeValue("Negative value. Value must be a positive integer")
    else:
        handshake = int(no_people * ((no_people-1) / 2))
    return handshake

if __name__ == "__main__":
    pass
    # print("test_normal_case_one", no_of_handshakes(2)) # 1
    # print("test_normal_case_two", no_of_handshakes(3)) # 3
    # print("test_normal_case_three", no_of_handshakes(20)) # 190
    # print("test_one_person", no_of_handshakes(1)) # 0
    # print("test_no_people", no_of_handshakes(0)) # 0
    # print("test_large_number_of_people", no_of_handshakes(10000)) # 49995000
    # print("test_negative_value", no_of_handshakes(-1)) # NegativeValue
    # print("test_invalid_input_type", no_of_handshakes("three")) # InvalidInput
    # print("test_extra_spaces", no_of_handshakes( 3 )) # 3
    # print("test_float_input", no_of_handshakes(3.5)) # InvalidInput
    # print("test_special_characters", no_of_handshakes("$%")) # InvalidInput
