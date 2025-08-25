from bitcoinlib.wallets import Wallet
import requests

def generate_wallet():
    wallet = Wallet.create("my_wallet")
    address = wallet.get_key().address
    private_key = wallet.get_key().wif()
    return address, private_key

def check_balance(address):
    API_URL = f"https://blockchain.info/q/addressbalance/{address}"
    response = requests.get(API_URL)
    if response.status_code == 200:
        satoshis = int(response.text)
        return satoshis / 100_000_000  # Convert to BTC
    return None

def sign_transaction(private_key, tx_data):
    # Placeholder: Use bitcoinlib for signing (simplified)
    print(f"Signing transaction with key: {private_key}")
    # Add real signing logic here (e.g., wallet.sign(tx_data))
    return "Signed TX: [dummy_hash]"

if __name__ == "__main__":
    addr, priv = generate_wallet()
    print(f"Generated Address: {addr}")
    print(f"Private Key: {priv}")
    
    balance = check_balance(addr)
    if balance is not None:
        print(f"Balance: {balance} BTC")
    
    # Example signing
    sign_transaction(priv, "dummy_tx_data")