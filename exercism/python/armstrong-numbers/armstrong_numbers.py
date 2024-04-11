def is_armstrong_number(number: int) -> bool:
    """
    This function identifies if the provided number is a armstrong number
    
    :number: int - number to be analyzed if its a armstrong number or not
    :return: bool - true if a number is a armstrong number and false if isn`t
    """

    # 1. Convert the number to string for iterating 
    str_number = str(number)
    
    # 2. Create a variable to store the iteration results
    power_digitis_sum = 0
    
    # 2.1 Get and store the lenght of the number 
    number_lenght = len(str_number)

    # 3. Iterate in the digits of the number, in which for each digit, we will power the current digit by number lenght
    power_digitis_sum = sum(int(digit)**number_lenght for digit in str_number)
    # DEPRECIATED
    # for digit in str_number: --> The only way I tha I was able to use the sum() built in function was with the for loop comprehension
        # int_digit = int(digit) --> I can use the int() function directly in the power calculation [Feedback from IsaacG]
        # digit_power = int(digit)**number_lenght

    # 4. Sum the iteration results in the variable 
        # power_digitis_sum += digit_power --> Instead of using this type of sum, 
        #                                      I can use the built in function to sum directly in the digit_power variable to calculate

    # 5. Compare the number providade with the iteration sum variable and get to a conclusion based on the following condition:
    # 5.1 If the number is different than the iterarion sums so its not a armstrong number, but if it is equal then is a armstrong number
    return power_digitis_sum == number

