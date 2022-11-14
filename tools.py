#  todo format chart bracket printing

#  Basic functioning

def get_compound(money: int, days: int, int_rate: float) -> list:
    """
    Get the compound interest of your investments
    :param money: amount of money it will be invested
    :param days: how many days the money will be doing trading
    :param int_rate: daily profit interest
    :return: a list that contains the result of the compound gains
    """
    counter = money
    data = [money]
    for i in range(0, days):
        counter = counter * int_rate
        data.append(round(counter, 3))
    return data


def params_io() -> list:
    """
    Parameters input function
    :return:
    """
    money = int(input("Insert the initial amount of money to be invested: \n")) 
    days = int(input("Insert how much days the money will be invested: \n"))
    int_rate = 1.00 + (float(input("Insert interest rate per day: \n")) / 100)
    detail = input("Detail of your data: \n t: total \n d: daily \n")

    if len(detail) > 1:
        raise Exception("The length of the detail input must be 1 \n example: ¨m¨")

    params = [money, days, int_rate, detail]
    return params


#  Chart functions

def border(length):
    """
    Borders of the compound gain chart
    :param length: length of the chart
    :return: 0 if everything worked fine
    """
    print("-" * length)
    return 0


def cells(value) -> str:
    """
    Lines of the chart
    :param value: value to be replaced in the specific cell of the chart
    :return: string that will contain the cell
    """
    cell = f"| {value} |"
    return cell


def lines(data: list, freq: list):
    for i in range(0, len(data)):
        line = cells(freq[i]) + cells(data[i])
        print(line)
    return 0


#  Type of detailed information functions

def total(data: list):
    text1 = "|  Total  |"
    text2 = cells(data[-1])

    border(len(text1) + len(text2))
    print(text1 + text2)

    border(len(text1) + len(text2))
    return 0


def daily(data: list):
    sum_total = "|  Total  |"
    days = ["day" + str(num) for num in range(0, len(data))]

    border(length=len(sum_total) + len(cells(data[-1])))
    print(cells("Days") + cells("Gains"))
    border(length=len(sum_total) + len(cells(data[-1])))
    lines(data, days)
    border(length=len(sum_total) + len(cells(data[-1])))
    print(sum_total + cells(data[-1]))

    return 0


def format_data(data: list, detail="t"):
    if detail == "t":
        total(data)
    elif detail == "d":
        daily(data)


def gains():
    params = params_io()
    data = get_compound(params[0], params[1], params[2])
    format_data(data, params[3])
    return 0
