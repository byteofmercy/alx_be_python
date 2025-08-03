from simple_calculator import add, subtract, multiply, divide

def main():
    print("Simple CLI Calculator")
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operation (+, -, *, /): ").strip()
        num2 = float(input("Enter second number: "))

        if operator == '+':
            result = add(num1, num2)
        elif operator == '-':
            result = subtract(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)
        else:
            print("Invalid operator.")
            return

        print(f"Result: {result}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")
    except ZeroDivisionError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
