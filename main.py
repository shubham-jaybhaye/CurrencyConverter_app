with open('currencyData.txt') as f:
	lines = f.readlines()

currencyDict = {}

for line in lines:
    print(line)
    print('done')
    parsed = line.split("=")
    currencyDict[parsed[0]] = parsed[1]
amount = float(input("Enter amount:\n"))
print("Enter the name of the currency you want to convert this amount to? Available Options:\n")
[print(item) for item in currencyDict.keys()]
currency = input("Please enter one of these values: \n")
print(f"{amount} {currency[:3]} is equal to {round(amount *float(currencyDict[currency]),2 )} {currency[3:]}")