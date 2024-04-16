def steps(number):
    step = 0
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    while number != 1:
        if number%2 == 0:
            number = number/2
            step += 1
        else:
            number = number*3+1
            step += 1
    return step
steps(12)
    # [number/2 if number%2 == 0 else number*3+1 for step, element in range(2)] 
    # return 
