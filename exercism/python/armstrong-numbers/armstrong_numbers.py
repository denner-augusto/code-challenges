def is_armstrong_number(number = 370):
    """

    :number: int - number to be analyzed if its a armstrong number or not
    :return: bool - true if a number is a armstrong number and false if isn`t
    
    Function: is_armstrong_number
    This function identifies if the SUM of the DIGITS of a number which each sum of digits elevated by the lenght of the number 
    is equal to the number, then its a armstrong number
    
    9 | len(9) = 1 | 9^len(9) = number
    """

    # 1. Get and store the lenght of the number 
    number_lenght = len(str(number))
    
    # 2. Create a variable to store the iteration results
    power_digitis_sum = 0
    
    # 2.1 Convert the number to string for iterating 
    str_number = str(number)

    # 3. Iterate in the digits of the number, in which for each digit, we will power the current digit by number lenght
    for digit in range(number_lenght):
        int_digit = int(str_number[digit])
        digit_power = int_digit**number_lenght
    
    # 4. Sum the iteration results in the variable 
        power_digitis_sum += digit_power 

    # 5. Compare the number providade with the iteration sum variable and get to a conclusion based on the following condition:
    if(power_digitis_sum == number):
    # 5.1 If the number is different than the iterarion sums so its not a armstrong number, but if it is equal then is a armstrong number
        result = True
    else:
        result = False

    return result
