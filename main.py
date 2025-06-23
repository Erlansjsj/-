
import time
import requests

def ping_binance():
    for i in range(3):
        start = time.time()
        try:
            requests.get("https://api.binance.com/api/v3/time", timeout=5)
            end = time.time()
            print(f"Ping to Binance API: {(end - start) * 1000:.2f} ms")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    ping_binance()
