# ChainForge Architecture

This diagram illustrates how client applications interact with the ChainForge platform via REST API endpoints and RPC nodes.

```mermaid
sequenceDiagram
    autonumber
    actor Client as dApp Client / SDK
    participant API as REST Gateway
    participant Node as Validator Node
    participant State as Ledger State DB

    Client->>API: POST /v1/transactions (Signed Tx Payload)
    API->>Node: Validate & Broadcast
    Node->>State: Write State Transition
    State-->>Node: Confirmation
    Node-->>API: Tx Hash & Block Index
    API-->>Client: 202 Accepted { "tx_hash": "0x7a8..." }