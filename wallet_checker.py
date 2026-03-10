import requests
import argparse
from datetime import datetime

def get_price(coin_id: str) -> float:
    """Fetch approximate USD price from CoinGecko (public, no key)."""
    try:
        resp = requests.get(
            f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd",
            timeout=5
        )
        return resp.json().get(coin_id, {}).get("usd", 0.0)
    except:
        return 0.0

def check_btc(address: str, limit: int = 5):
    """Bitcoin wallet checker using blockchain.info (public API, no key)."""
    print("\n=== Bitcoin Wallet Checker ===")
    url = f"https://blockchain.info/rawaddr/{address}?limit={limit}"
    try:
        data = requests.get(url, timeout=10).json()
        
        balance_btc = data.get("final_balance", 0) / 100_000_000
        price = get_price("bitcoin")
        usd_value = balance_btc * price if price else 0
        
        print(f"Address: {address}")
        print(f"💰 Balance: {balance_btc:.8f} BTC (~ ${usd_value:,.2f} USD)")
        print(f"Total transactions: {data.get('n_tx', 0)}\n")
        
        print("📜 Last Transactions:")
        for i, tx in enumerate(data.get("txs", [])[:limit]):
            ts = datetime.fromtimestamp(tx.get("time", 0))
            tx_hash = tx.get("hash", "N/A")
            print(f"  {i+1}. {ts.strftime('%Y-%m-%d %H:%M')}")
            print(f"     Hash: {tx_hash}")
            print(f"     View: https://blockchain.com/btc/tx/{tx_hash}")
            print("     " + "-" * 50)
    except Exception as e:
        print(f"❌ Error fetching BTC data: {e}")

def check_eth(address: str, limit: int = 5):
    """Ethereum wallet checker using Ethplorer (public 'freekey', no signup)."""
    print("\n=== Ethereum Wallet Checker ===")
    base = "https://api.ethplorer.io"
    api_key = "freekey"
    
    # 1. Portfolio (native ETH + all tokens)
    info_url = f"{base}/getAddressInfo/{address}?apiKey={api_key}"
    try:
        info = requests.get(info_url, timeout=10).json()
        
        eth_data = info.get("ETH", {})
        eth_bal = eth_data.get("balance", 0)
        price = get_price("ethereum")
        usd_value = eth_bal * price if price else 0
        
        print(f"Address: {address}")
        print(f"💰 ETH Balance: {eth_bal:.6f} ETH (~ ${usd_value:,.2f} USD)")
        
        # Show top tokens (if any)
        tokens = info.get("tokens", [])
        if tokens:
            print(f"🪙 Token Holdings ({len(tokens)} found):")
            for t in tokens[:5]:  # top 5
                token = t.get("tokenInfo", {})
                bal = float(t.get("balance", 0)) / (10 ** int(token.get("decimals", 18)))
                symbol = token.get("symbol", "???")
                if bal > 0:
                    print(f"   • {bal:,.4f} {symbol}")
        else:
            print("   No ERC-20 tokens found.")
    except Exception as e:
        print(f"❌ Portfolio error: {e}")
        eth_bal = 0
    
    # 2. Recent native transactions
    tx_url = f"{base}/getAddressTransactions/{address}?apiKey={api_key}&limit={limit}"
    try:
        tx_data = requests.get(tx_url, timeout=10).json()
        print(f"\n📜 Last {len(tx_data)} Native Transactions:")
        for tx in tx_data[:limit]:
            ts = datetime.fromtimestamp(tx.get("timestamp", 0))
            value_eth = float(tx.get("value", 0)) / 1e18
            direction = "← IN" if tx.get("to", "").lower() == address.lower() else "→ OUT"
            hash_short = tx.get("hash", "")[:10] + "..."
            print(f"  {ts.strftime('%Y-%m-%d %H:%M')}  {direction}  {value_eth:.6f} ETH")
            print(f"     Hash: {hash_short}  |  View: https://etherscan.io/tx/{tx.get('hash')}")
            print("     " + "-" * 55)
    except Exception as e:
        print(f"❌ Transactions error: {e}")

def main():
    parser = argparse.ArgumentParser(description="Crypto Wallet Info Checker (BTC + ETH) - No API key needed!")
    parser.add_argument("address", help="Wallet address (auto-detects BTC or ETH)")
    parser.add_argument("--limit", type=int, default=5, help="Number of recent transactions (default: 5)")
    args = parser.parse_args()
    
    address = args.address.strip()
    limit = args.limit
    
    # Auto-detect chain
    addr_lower = address.lower()
    if addr_lower.startswith("0x") and len(addr_lower) == 42:
        check_eth(address, limit)
    elif (address.startswith(("1", "3", "bc1")) and 26 <= len(address) <= 62) or len(address) == 34:
        check_btc(address, limit)
    else:
        print("❌ Could not detect chain. Supported formats:")
        print("   • Ethereum: 0x... (42 characters)")
        print("   • Bitcoin: 1..., 3..., bc1...")

if __name__ == "__main__":
    print("🚀 Crypto Wallet Info Checker by Wallet Address")
    print("   Supports BTC & ETH • Last transactions • USD values • No signup/keys!")
    print("=" * 70)
    main()
