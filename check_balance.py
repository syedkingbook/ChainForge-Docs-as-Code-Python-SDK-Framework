Python
import os
from chainforge import ChainForge

client = ChainForge(api_key=os.environ["CHAINFORGE_API_KEY"])
bal = client.accounts.get_balance("0x71C7656EC7ab88b098defB75187401B5f6d8976F")
print(f"Balance: {bal.balanceFormatted} {bal.symbol} at block {bal.blockNumber}")