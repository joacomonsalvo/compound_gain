def get_compound(money: int, days: int, int_rate: float, detail="total"):
    """
    Get the compound interest of your investments
    :param money: amount of money it will be invested
    :param days: how many days the money will be doing trading
    :param int_rate: daily profit interest
    :param detail: detail level (total, daily, weekly or monthly)
    :return: a variable that contains the result of the compound gains
    """
    counter = money
    for i in range(0, days):
        counter = counter * int_rate
    return counter


def params_io():
    """
    Parameters input function
    :return:
    """
    money = int(input("Insert the initial amount of money to be invested: \n")) 
    days = int(input("Insert how much days the money will be invested: \n"))
    int_rate = 1.00 + (float(input("Insert interest rate per day: \n")) / 100)
    params = [money, days, int_rate]
    return params


def border(length):
    print("-" * length)
    return 0


def line(value):
    lines = f"| {value} |"
    return lines


def print_gains():
    params = params_io()
    return 0
