'''This is a simple calculator for revise and update my coding skill and logical thinking'''
'''Rule is must be use OOP, Conditions, Functions, Decorators'''
def calculator_decorator(func):
    def wrapper():
        print("--- Simple Calculator ---")
        try:
            num1 = float(input("Enter first number: "))
            operator = input("Enter operator (+, -, *, /): ")
            num2 = float(input("Enter second number: "))
            result = func(num1, operator, num2)
            print(f"Result: {result}")
        except ValueError:
            print("Error: Please enter valid numbers.")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
        print("-------------------------")
    return wrapper

@calculator_decorator
def calculate(n1, op, n2):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    elif op == '/':
        return n1 / n2
    else:
        return "Invalid Operator"

if __name__ == "__main__":
    calculate()
