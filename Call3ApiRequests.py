import requests
import time
import json

def get_temperature():
        start  = time.time()
        print("Fetching current temperature... Please wait.")
        time.sleep(2)  # Simulate a delay for better demonstration
        response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=28.61&longitude=77.23&current_weather=true")
        Alldata = response.json()
        temperature = Alldata["current_weather"]["temperature"]
        end = time.time()
        print(f"API call duration: {end - start} seconds")
        return temperature


def get_crypto_price():
        start  = time.time()
        print("Fetching cryptocurrency price... Please wait.")
        time.sleep(2)  # Simulate a delay for better demonstration
        response = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT")
        Alldata = response.json()
        symbol = Alldata["symbol"]
        price = Alldata["price"]
        end = time.time()
        print(f"API call duration: {end - start} seconds")
        return symbol, price

def get_jokes():
      start  = time.time()
      print("Fetching programming joke... Please wait.")
      time.sleep(2)  # Simulate a delay for better demonstration
      response = requests.get("https://v2.jokeapi.dev/joke/Programming")
      Alldata = response.json()
      joke = Alldata["setup"]
      end = time.time()
      print(f"API call duration: {end - start} seconds")
      return joke

def main():
    s1 = time.time()
    temp = get_temperature()
    print(f"The current temperature is: {temp}°C")
    symbol, price = get_crypto_price()
    print(f"The current price of {symbol} is: ${price}")
    joke = get_jokes()
    print(f"Here's a programming joke for you: {joke}")
    e1 = time.time()
    print(f"Total execution time: {e1 - s1} seconds")

if __name__ == "__main__":
    main()