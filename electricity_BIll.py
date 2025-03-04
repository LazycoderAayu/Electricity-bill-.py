import time

def print_decorated(text, symbol="*"):
    print(symbol * (len(text) + 10))
    print(f"{symbol * 5} {text} {symbol * 5}")
    print(symbol * (len(text) + 10))

def get_tariff(city, provider, units):
    tariffs = {
        "mumbai": {
            "adani": [
                (100, 4.00),
                (300, 5.76),
                (500, 9.66),
                (float('inf'), 10.76)
            ],
            "tata power": [
                (100, 3.93),
                (300, 5.18),
                (500, 10.74),
                (float('inf'), 11.48)
            ]
        },
        "delhi": {
            "bses": [
                (200, 3.00),
                (400, 4.50),
                (float('inf'), 6.00)
            ],
            "ndpl": [
                (200, 3.20),
                (400, 4.70),
                (float('inf'), 6.20)
            ]
        },
        "bangalore": {
            "bescom": [
                (100, 3.75),
                (300, 5.20),
                (500, 6.75),
                (float('inf'), 7.80)
            ]
        },
        "kolkata": {
            "cesc": [
                (100, 4.89),
                (300, 5.40),
                (500, 6.41),
                (float('inf'), 7.00)
            ]
        },
        "chennai": {
            "tneb": [
                (100, 3.50),
                (200, 4.60),
                (500, 6.60),
                (float('inf'), 8.00)
            ]
        },
        "pune": {
            "mahavitaran": [
                (100, 4.10),
                (300, 5.50),
                (500, 7.50),
                (float('inf'), 8.90)
            ]
        },
        "hyderabad": {
            "tsspdcl": [
                (100, 3.75),
                (200, 5.20),
                (400, 6.50),
                (float('inf'), 7.70)
            ]
        },
        "ahmedabad": {
            "torrent power": [
                (100, 4.00),
                (300, 5.50),
                (500, 6.80),
                (float('inf'), 7.90)
            ]
        },
        "lucknow": {
            "upcl": [
                (100, 3.90),
                (300, 5.40),
                (500, 6.70),
                (float('inf'), 7.80)
            ]
        },
        "jaipur": {
            "jvvnl": [
                (100, 4.15),
                (300, 5.60),
                (500, 6.90),
                (float('inf'), 8.00)
            ]
        },
        "bhopal": {
            "mppmcl": [
                (100, 3.85),
                (300, 5.30),
                (500, 6.60),
                (float('inf'), 7.70)
            ]
        },
        "patna": {
            "sbpdcl": [
                (100, 4.00),
                (300, 5.50),
                (500, 6.80),
                (float('inf'), 7.90)
            ]
        },
        "bhubaneswar": {
            "tpcodl": [
                (100, 3.95),
                (300, 5.40),
                (500, 6.70),
                (float('inf'), 7.80)
            ]
        }
    }
    
    city = city.lower()
    provider = provider.lower()
    
    if city in tariffs and provider in tariffs[city]:
        for limit, rate in tariffs[city][provider]:
            if units <= limit:
                return rate
    return None

def calculate_bill(units, rate):
    return units * rate

def main():
    print_decorated("Electricity Bill Calculator", "#")
    
    name = input("Enter your name: ")
    city = input("Enter your city: ")
    provider = input("Enter your electricity provider: ")
    
    try:
        units = float(input("Enter the number of units consumed: "))
    except ValueError:
        print("Invalid input for units. Please enter a numerical value.")
        return
    
    tariff = get_tariff(city, provider, units)
    
    if tariff is None:
        print("Invalid city, provider, or unit range! Please enter valid details.")
        return
    
    bill_amount = calculate_bill(units, tariff)
    
    time.sleep(1)
    print_decorated("Billing Details", "-")
    print(f"Name: {name}")
    print(f"City: {city.capitalize()}")
    print(f"Electricity Provider: {provider.capitalize()}")
    print(f"Units Consumed: {units} units")
    print(f"Tariff: ₹{tariff} per unit")
    print(f"Total Bill Amount: ₹{bill_amount:.2f}")
    print_decorated("Thank You!", "~")

if __name__ == "__main__":
    main()
