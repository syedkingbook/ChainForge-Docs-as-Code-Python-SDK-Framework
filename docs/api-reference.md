```markdown
# REST API Reference

The ChainForge REST API allows developers to submit transactions, inspect accounts, and query smart contracts on the testnet.

## Base URL
`https://testnet-api.chainforge.network/v1`

---

## Submit Transaction

`POST /v1/transactions`

Submits a signed transaction payload to the testnet pool.

### Request Body (`application/json`)

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `sender` | string | Yes | The 40-character hexadecimal wallet address. |
| `recipient` | string | Yes | The target contract or wallet address. |
| `amount` | string | Yes | Transfer value in `FORGE` units (as string to prevent overflow). |
| `payload` | string | No | Optional compiled smart contract call data. |

### Sample Request (cURL)

```bash
curl -X POST [https://testnet-api.chainforge.network/v1/transactions](https://testnet-api.chainforge.network/v1/transactions) \
  -H "Content-Type: application/json" \
  -d '{
    "sender": "0x1234567890abcdef1234567890abcdef12345678",
    "recipient": "0xcafebabe00000000000000000000000000000000",
    "amount": "100.50"
  }'