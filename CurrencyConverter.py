from currency_converter import CurrencyConverter
import pycountry
import time

c = CurrencyConverter()
i = 0

all_currencies = c.currencies

currency_dict = {}

print("Here are our currencies:")
for currency in all_currencies:
    i += 1
    print(f"{i}- {currency}")
    currency_dict[i] = currency

amount = float(input("pick the amount: "))
currency_one = int(input("pick a currency you want to convert: "))
print(f"{amount} {currency_dict[currency_one]}")

currency_two = int(input("pick a currency you want to convert: "))
print(currency_dict[currency_two])

print(
    f"converting {amount} {currency_dict[currency_one]} to {currency_dict[currency_two]}"
)

time.sleep(3)

converted_amount = c.convert(
    amount, currency_dict[currency_one], currency_dict[currency_two]
)

print(
    f"{amount} {currency_dict[currency_one]} = {round(converted_amount, 2)} {currency_dict[currency_two]}"
)
