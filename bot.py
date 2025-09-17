import os
import ccxt
from dotenv import load_dotenv

load_dotenv()

EXCHANGE   = os.getenv("EXCHANGE", "binance")
API_KEY    = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
SYMBOL     = os.getenv("SYMBOL", "BTC/USDT")

ex = getattr(ccxt, EXCHANGE)({
    "apiKey": API_KEY,
    "secret": API_SECRET,
    "enableRateLimit": True,
})

def main():
    ticker = ex.fetch_ticker(SYMBOL)
    print(f"Последняя цена {SYMBOL}: {ticker['last']}")

if __name__ == "__main__":
    main()
