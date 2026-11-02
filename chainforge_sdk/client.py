import os
import requests

class AccountsModule:
    def __init__(self, client):
        self.client = client

    def get_balance(self, address, block="latest"):
        """Calls GET /accounts/{address}/balance per API Reference section 5.3"""
        path = f"/accounts/{address}/balance"
        params = {"block": block} if block else {}
        return self.client._get(path, params=params)

class StatusModule:
    def __init__(self, client):
        self.client = client

    def get(self):
        """Calls GET /status per API Reference section 4.1"""
        return self.client._get("/status")

class ChainForge:
    def __init__(self, api_key=None, network="ember"):
        # Base REST URL from API Reference section 1.3
        self.base_url = "https://api.chainforge.example/v1"
        self.api_key = api_key or os.environ.get("CHAINFORGE_API_KEY")
        
        if not self.api_key:
            raise ValueError("API key must be provided or set in CHAINFORGE_API_KEY environment variable.")
            
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        # Bind modules matching the Developer Guide structure
        self.accounts = AccountsModule(self)
        self.status = StatusModule(self)
        
    def _get(self, path, params=None):
        url = self.base_url + path
        
        # --- LOCAL MOCK MODE FOR DOCUMENTATION PRACTICE ---
        if "chainforge.example" in self.base_url:
            if "/status" in path:
                return DotDict({
                    "network": "ember-testnet",
                    "chainId": 9403,
                    "status": "healthy",
                    "blockNumber": 1420589
                })
            elif "balance" in path:
                # Extract address from path if needed, or return sample data
                return DotDict({
                    "address": "0x71C7656EC7ab88b098defB75187401B5f6d8976F",
                    "balance": "1500000000000000000",
                    "balanceFormatted": "1.5",
                    "symbol": "tFORGE",
                    "blockNumber": 1420589
                })
        # --------------------------------------------------

        response = requests.get(url, headers=self.headers, params=params, timeout=15)
        
        if not response.ok:
            try:
                err_data = response.json().get("error", {})
                code = err_data.get("code", "unknown_error")
                message = err_data.get("message", response.text)
                req_id = err_data.get("requestId", "unknown")
                raise RuntimeError(f"API Error {response.status_code} [{code}]: {message} (RequestId: {req_id})")
            except json.JSONDecodeError:
                response.raise_for_status()
                
        return DotDict(response.json())

class DotDict(dict):
    """Allows dot notation access to dictionary keys (e.g., bal.balance_formatted)"""
    def __getattr__(self, attr):
        if attr in self:
            return self[attr]
        raise AttributeError(f"'DotDict' object has no attribute '{attr}'")
    
    def __setattr__(self, attr, value):
        self[attr] = value