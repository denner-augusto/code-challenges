def is_armstrong_number(number: int) -> bool:
    """
    Identify if the provided number is a armstrong number
    
    :number: int - Input number provided by the user
    :return: bool - Boolean return with True for a armstrong number and False if is not.
    """
    str_number = str(number)
    
    # 3. Iterate in the digits of the number, in which for each digit, we will power the current digit by number lenght
    power_digits_sum = sum(int(digit)**len(str_number) for digit in str_number)

    return power_digits_sum == number

