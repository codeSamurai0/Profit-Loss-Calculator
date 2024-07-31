# This program is made to accept any kind of input without throwing error.

# Modules

import sys
import time

def main():

	while True:
		try:
			print("Press ctrl+c to quit!\n")

			# Taking in inputs for price and amount

			buying_price = float(input("Type in the buying price: $"))
			selling_price = float(input("Type in the selling price: $"))
			amount = float(input("Type in the amount: $"))

			# Doing calculations and printing out profit/loss.

			buy_price = amount * buying_price
			sell_price = amount * selling_price
			profit = sell_price - buy_price	

			print(f"\nBuying Price: ${buying_price} \nSelling Price: ${selling_price} \nAmount: {amount} \nProfit/Loss: ${profit}\n")

		# Resetting if the user types in a negative number or some alphabet

		except (ValueError, UnboundLocalError):
			print("Please type in a number > 0")
			print("Resetting...")
			continue

		# Quitting the program if the user presses Ctrl + C

		except (KeyboardInterrupt):
			print("\nQuitting...")
			time.sleep(1)
			sys.exit()

main()
