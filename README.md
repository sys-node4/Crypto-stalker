# Crypto Wallet Info Checker

A lightweight, **no-API-key-required** Python CLI tool to quickly check crypto wallet balances, approximate USD value, token holdings (for Ethereum), and recent transactions.

Currently supports:
- **Bitcoin (BTC)**
- **Ethereum (ETH)** + ERC-20 tokens

Uses only free public endpoints → perfect for personal use, quick checks, or scripting.

## Features

- Auto-detects BTC or ETH address format
- Shows current **balance** + approximate **USD value** (via CoinGecko)
- Displays **last N transactions** with date, direction (IN/OUT), amount & explorer link
- Ethereum: also shows top ERC-20 token balances
- Zero dependencies beyond `requests`
- Clean, human-readable console output
- No signup, no API keys, no rate-limit worries for casual use

## Requirements

- Python 3.6+
- `requests` library

```bash
pip install requests
```

## Installation

Clone the repository:

```bash
git clone https://github.com/sys-node4/crypto-wallet-checker.git
cd crypto-wallet-checker
```

Or download the single file directly:

```bash
curl -O https://raw.githubusercontent.com/sys-node4/crypto-wallet-checker/main/wallet_checker.py
```

(If you prefer, just copy-paste the code into a file named `wallet_checker.py`.)

## Usage

```bash
python wallet_checker.py <WALLET_ADDRESS> [--limit N]
```

### Examples

```bash
# Ethereum address
python wallet_checker.py 0x742d35Cc6634C0532925a3b844Bc454e4438f44e

# Bitcoin address
python wallet_checker.py bc1qar0srrr7xfkvy5l643lydnw9re59gtzzwf5mdq --limit 10

# Another popular ETH address
python wallet_checker.py 0x690b9a9e9aa1c9db991c28d3b210986696fa62a8
```

**Sample output**:

```
🚀 Crypto Wallet Info Checker by Wallet Address
   Supports BTC & ETH • Last transactions • USD values • No signup/keys!
======================================================================

=== Ethereum Wallet Checker ===
Address: 0x742d35Cc6634C0532925a3b844Bc454e4438f44e
💰 ETH Balance: 124.837492 ETH (~ $312,094.23 USD)
🪙 Token Holdings (8 found):
   • 1,245,672.84 USDT
   • 458,219.11 USDC
   • 0.00012 WBTC

📜 Last 5 Native Transactions:
  2025-03-09 14:22  ← IN  15.420000 ETH
     Hash: 0x8f3b...a9d2  |  View: https://etherscan.io/tx/0x8f3b...
     -------------------------------------------------------
  2025-03-08 09:17  → OUT  7.500000 ETH
     Hash: 0x4e7c...f12b  |  View: https://etherscan.io/tx/0x4e7c...
     -------------------------------------------------------
...
```

## Supported Chains (so far)

| Chain     | Address format starts with     | Balance | Tokens | Last tx | Explorer links     |
|-----------|--------------------------------|---------|--------|---------|--------------------|
| Bitcoin   | `1…`, `3…`, `bc1…`             | ✓       | —      | ✓       | blockchain.com     |
| Ethereum  | `0x…` (42 chars)               | ✓       | ✓      | ✓       | etherscan.io       |

## Planned / Possible Future Features

- Solana support
- Polygon, BSC, Arbitrum
- `--json` output for automation
- Simple web interface (Streamlit / Flask)
- Watch mode with periodic checks

## Limitations & Notes

- Public endpoints may have rate limits on very heavy use
- Price data from CoinGecko (free tier) — can occasionally be delayed
- Ethereum token list shows non-zero balances only
- Always double-check important values on official block explorers
- Not intended for production-grade monitoring or high-frequency usage

## Contributing

Pull requests are welcome!  
Ideas especially appreciated for:
- Adding new blockchains
- Improved error handling & retries
- Export options (JSON, CSV)
- UI enhancements

## License

[MIT License](LICENSE) — free to use, modify, and share.

---

Made with ❤️ for fast wallet lookups  
Happy checking! 🚀
```

