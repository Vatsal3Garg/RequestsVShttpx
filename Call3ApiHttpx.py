import httpx 
import asyncio
import time

async def fetch_temp(client):
    s1  = time.time()
    print("Fetching temperature... Please wait.")
    await asyncio.sleep(2)  # Simulate a delay for better demonstration
    response = await client.get("https://api.open-meteo.com/v1/forecast?latitude=28.61&longitude=77.23&current_weather=true")
    Alldata = response.json()
    e1 = time.time()
    
    return Alldata["current_weather"]["temperature"]



async def fetch_crypto_price(client):
        s2  = time.time()
        print("Fetching cryptocurrency price... Please wait.")
        await asyncio.sleep(2)  # Simulate a delay for better demonstration
        response = await client.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT")
        Alldata = response.json()
        symbol = Alldata["symbol"]
        price = Alldata["price"]
        e2 = time.time()
        
        return f"{symbol}: {price} USD"

async def fetch_jokes(client):
      s3  = time.time()
      print("Fetching programming joke... Please wait.")
      await asyncio.sleep(2)  # Simulate a delay for better demonstration
      response = await client.get("https://api.chucknorris.io/jokes/random")
      Alldata = response.json()
      joke = Alldata["value"]
      e3 = time.time()
     
      return joke



async def main():
    s4 = time.time()
    async with httpx.AsyncClient() as client:
        temp , crypto_price , joke = await asyncio.gather(
            fetch_temp(client),
            fetch_crypto_price(client),
            fetch_jokes(client)
        )
    print("\n---------------")    
    print("\n--- Results ---")
    print("\n---------------")   
    print("\n") 

    print(f"Current temperature: {temp}°C")
    print(f"Current BTC price: {crypto_price}")
    print(f"Programming joke: {joke}")
    e4 = time.time()
    print(f"\nTotal execution time: {e4 - s4} seconds")
asyncio.run(main())    