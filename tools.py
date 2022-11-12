def get_compound(money: int, days: int, int_rate: float):
    """
    Get the compound interest of your investments
    :param money: amount of money it will be invested
    :param days: how many days the money will be doing trading
    :param int_rate: daily profit interest
    :return: a variable that contains the result of the compound gains
    """
    counter = money
    data = [money]
    for i in range(0, days):
        counter = counter * int_rate
        data.append(counter)
    return data


def params_io():
    """
    Parameters input function
    :return:
    """
    money = int(input("Insert the initial amount of money to be invested: \n")) 
    days = int(input("Insert how much days the money will be invested: \n"))
    int_rate = 1.00 + (float(input("Insert interest rate per day: \n")) / 100)
    detail = input("Detail of your data: \n t: total \n d: daily \n w: weekly \n m: monthly")

    if len(detail) > 1:
        raise Exception("The length of the detail input must be 1 \n example: ¨m¨")

    params = [money, days, int_rate, detail]
    return params


def border(length):
    print("-" * length)
    return 0


def lines(value):
    line = f"| {value} |"
    return line


def format_data(data: list, detail="t"):
    pass


def print_gains():
    params = params_io()
    data = get_compound(params[0], params[1], params[2])
    format_data(data, params[3])
    #  Print data with border and lines
    return 0
