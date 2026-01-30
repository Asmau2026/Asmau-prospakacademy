
celsius_str = input("Enter temperature in Celsius: ")


celsius_temp = float(celsius_str)

# F = (C * 9/5) + 32
fahrenheit_temp = (celsius_temp * 9/5) + 32

print(f"{celsius_temp} degrees Celsius is equal to {fahrenheit_temp:.1f} degrees Fahrenheit.")