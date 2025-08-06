#!/usr/bin/python3

def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)  # ✅ Conversion to float
        denominator = float(denominator)  # ✅ Conversion to float
        result = numerator / denominator
        return f"The result of the division is {result}"
    except ZeroDivisionError:  # ✅ Handles division by zero
        return "Error: Cannot divide by zero."
    except ValueError:  # ✅ Handles non-numeric input
        return "Error: Please enter numeric values only."
