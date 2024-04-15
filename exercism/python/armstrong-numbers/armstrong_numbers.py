def is_armstrong_number(number: int) -> bool:
    """
    Identify if the provided number is a armstrong number
    
    :number: int - number to be analyzed if its a armstrong number or not
    :return: bool - true if a number is a armstrong number and false if isn`t
    """
    str_number = str(number)
    
    # 3. Iterate in the digits of the number, in which for each digit, we will power the current digit by number lenght
    power_digitis_sum = sum(int(digit)**len(str_number) for digit in str_number)

    return power_digitis_sum == number

