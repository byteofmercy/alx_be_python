# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Conversion functions
def convert_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_celsius_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Main program
if __name__ == "__main__":
    print("Temperature Conversion Tool")
    print("Choose conversion:")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")

    choice = input("Enter 1 or 2: ")

    try:
        if choice == "1":
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = convert_fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F is {celsius:.2f}°C")
        elif choice == "2":
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = convert_celsius_to_fahrenheit(celsius)
            print(f"{celsius}°C is {fahrenheit:.2f}°F")
        else:
            print("Invalid choice. Please enter 1 or 2.")
    except ValueError:
        print("Invalid input. Please enter a number.")

