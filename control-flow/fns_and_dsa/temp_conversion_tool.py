# Global conversion factors
FAHRENHEIT_TO_CELSIUS = lambda f: (f - 32) * 5/9
CELSIUS_TO_FAHRENHEIT = lambda c: (c * 9/5) + 32
CELSIUS_TO_KELVIN = lambda c: c + 273.15
KELVIN_TO_CELSIUS = lambda k: k - 273.15

# Conversion function
def convert_temperature(value, from_unit, to_unit):
    try:
        value = float(value)
    except ValueError:
        raise ValueError("Invalid numeric input.")

    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit == to_unit:
        return value

    if from_unit == "celsius":
        if to_unit == "fahrenheit":
            return CELSIUS_TO_FAHRENHEIT(value)
        elif to_unit == "kelvin":
            return CELSIUS_TO_KELVIN(value)
    elif from_unit == "fahrenheit":
        if to_unit == "celsius":
            return FAHRENHEIT_TO_CELSIUS(value)
        elif to_unit == "kelvin":
            celsius = FAHRENHEIT_TO_CELSIUS(value)
            return CELSIUS_TO_KELVIN(celsius)
    elif from_unit == "kelvin":
        if to_unit == "celsius":
            return KELVIN_TO_CELSIUS(value)
        elif to_unit == "fahrenheit":
            celsius = KELVIN_TO_CELSIUS(value)
            return CELSIUS_TO_FAHRENHEIT(celsius)

    raise ValueError("Invalid conversion units.")

# User interaction
def main():
    print("Temperature Conversion Tool")
    try:
        temp_value = input("Enter the temperature value to convert: ")
        from_unit = input("Convert from (Celsius, Fahrenheit, Kelvin): ")
        to_unit = input("Convert to (Celsius, Fahrenheit, Kelvin): ")
        result = convert_temperature(temp_value, from_unit, to_unit)
        print(f"{temp_value} {from_unit.capitalize()} is {round(result, 2)} {to_unit.capitalize()}")
    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == "__main__":
    main()
