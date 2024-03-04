# conversions_refactored.py

def convert(fromUnit, toUnit, value):
    """
    Convert value from one unit to another.

    Parameters:
    - fromUnit (str): The unit we are converting from.
    - toUnit (str): The unit we are converting to.
    - value (float): The value of fromUnit we are converting from.

    Returns:
    - float: The converted value.
    """

    if fromUnit == toUnit:
        return value

    if fromUnit == "Fahrenheit" and toUnit == "Celsius":
        # Fahrenheit to Celsius conversion
        converted_value = (value - 32) * 5 / 9
    elif fromUnit == "Celsius" and toUnit == "Fahrenheit":
        # Celsius to Fahrenheit conversion
        converted_value = (value * 9 / 5) + 32
    elif fromUnit == "Celsius" and toUnit == "Kelvin":
        # Celsius to Kelvin conversion
        converted_value = value + 273.15
    elif fromUnit == "Kelvin" and toUnit == "Celsius":
        # Kelvin to Celsius conversion
        converted_value = value - 273.15
    elif fromUnit == "Fahrenheit" and toUnit == "Kelvin":
        # Fahrenheit to Kelvin conversion
        converted_value = (value + 459.67) * 5 / 9
    elif fromUnit == "Kelvin" and toUnit == "Fahrenheit":
        # Kelvin to Fahrenheit conversion
        converted_value = (value * 9 / 5) - 459.67
    else:
        raise ValueError("Invalid conversion")

    return converted_value
