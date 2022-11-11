def compound_gain(money:int, days:int, int_rate:float):
    counter = money
    for i in range(0, days):
        counter = counter * int_rate
    return counter


if __name__ == "__main__":
    money = int(input("Insert the initial amount of money to be invested: \n")) 
    days = int(input("Insert how much days the money will be invested: \n"))
    int_rate = 1.00 + (float(input("Insert interest rate per day: \n")) / 100)
    print(compound_gain(money, days, int_rate))
