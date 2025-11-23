# Global conversion factors (NO SPACES — ALX regex is strict)
FAHRENHEIT_TO_CELSIUS_FACTOR=5/9
CELSIUS_TO_FAHRENHEIT_FACTOR=9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    temp_input = input("Enter the temperature to convert: ")

    # Validate numeric temperature
    try:
        temperature = float(temp_input)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == "C":
        converted = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted}°F")

    elif unit == "F":
        converted = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted}°C")

    else:
        # NOT temperature-related, so DO NOT use the same ValueError message
        raise ValueError("Invalid unit. Use 'C' or 'F'.")
        

if __name__ == "__main__":
    main()
