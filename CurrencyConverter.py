import requests


SUPPORTED_CURRENCIES = {
    "EUR": "European euro",
    "USD": "US dollar",
    "GBP": "Pound sterling",
    "BRL": "Brazilian real"
}


CURRENCY_CODES = {
    1: "EUR",
    2: "USD",
    3: "GBP",
    4: "BRL"
}


def get_exchange_rate(base_currency, target_currency):
    if not (base_currency in SUPPORTED_CURRENCIES.keys()):
        raise ValueError("base currency {} not supported".format(base_currency))
    if not (target_currency in SUPPORTED_CURRENCIES.keys()):
        raise ValueError("target currency {} not supported".format(target_currency))

    if base_currency == target_currency:
        return 1

    api_uri = "https://api.fixer.io/latest?base={}&symbols={}".format(base_currency, target_currency)
    api_response = requests.get(api_uri)

    if api_response.status_code == 200:
        return api_response.json()["rates"][target_currency]


if __name__ == '__main__':
    print("Welcome to Currency Converter")

    amount = float(input("Enter the amount you wish to convert: "))

    print("Choose a base currency among our supported currencies:")
    while True:
        for code, currency in CURRENCY_CODES.items():
            print("code {}: base {}".format(code, currency))
        base_currency_code = int(input("Please digit the code: "))
        if base_currency_code in CURRENCY_CODES.keys():
            break
        else:
            print("Invalid code")
    base_currency = CURRENCY_CODES[base_currency_code]

    print("Choose a target currency among our supported currencies:")
    while True:
        for code, currency in CURRENCY_CODES.items():
            print("code {}: target {}".format(code, currency))
        target_currency_code = int(input("Please digit the code: "))
        if target_currency_code in CURRENCY_CODES.keys():
            break
        else:
            print("Invalid code")
    target_currency = CURRENCY_CODES[target_currency_code]

    exchange_rate = get_exchange_rate(base_currency, target_currency)

    print("{} {} is {} {}".format(amount, base_currency, amount * exchange_rate, target_currency))
