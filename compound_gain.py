def compound_gain(money:int, days:int, int_rate:float):
    counter = money
    for i in range(0, days):
        counter = counter * int_rate
    return counter
