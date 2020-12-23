

def multiply():
    try:
        number1 = float(input("Please enter a number:"))
        number2 = float(input("NOw please enter a second number:"))
        answer = number1 * number2
        return answer
    except ValueError as error:
        print(error)


def division():
    try:
        number1 = float(input("Please enter a number:"))
        switch = True
        while switch:
            number2 = float(input("Now please enter a second number:"))
            if number2 != 0:
                switch = False
            else:
                print("Can't divide by 0")
        answer = number1 / number2
        return answer
    except ValueError as error:
        print(error)
    except ZeroDivisionError as error:
        print(error)


if __name__ == '__main__':
    print("The answer is:", multiply())
    print("The answer is:", division())

my_variable = """This is a variable
created only for testing
the modules usage"""
