from currency_converter import CurrencyConverter
import pycountry

# Create an instance of the CurrencyConverter class
c = CurrencyConverter()
i = 0

# Get the list of all available currencies
all_currencies = c.currencies

# Print the list of currencies
print("pick a currency you want to convert :")
for currency in all_currencies:
    i += 1
    print(f"{i}- {currency}")
