
# Aave V2 Wallet Credit Scoring

This project provides a **credit scoring system for wallets interacting with the Aave V2 protocol**. Each wallet is assigned a **credit score between 0 and 1000** based on historical transaction behavior.

Higher scores indicate **responsible and reliable usage** (e.g., timely repayments, healthy deposits). Lower scores suggest **risky or bot-like activity** (e.g., liquidations, unbalanced borrowing).

## 🚀 Features
- Processes raw transaction-level JSON data.
- Aggregates wallet activity (deposits, borrows, repayments, liquidations).
- Assigns a credit score to each wallet based on transparent rules.
- Outputs a clean CSV for downstream analysis or integration.

## 📊 Scoring Logic
| Feature                       | Impact on Score                                        |
|--------------------------------|--------------------------------------------------------|
| **Deposit/Borrow Ratio**       | High ratio → safer behavior (score ↑)                  |
| **Repayment Ratio**            | Full repayment → responsible (score ↑)                 |
| **Liquidation Events**         | Liquidations → risky (score ↓)                         |
| **Active Duration**            | Longer activity → higher trust (score ↑)               |
| **Transaction Count**          | Too few txns → penalized as bot (score ↓)              |

Scores are clamped between **0 (worst)** and **1000 (best)**.

## 🛠 How to Use
### 1️⃣ Install dependencies
```
pip install pandas
```

### 2️⃣ Run the script
```
python wallet_credit_score.py user-wallet-transactions.json wallet_credit_scores.csv
```

### 📥 Input
- `user-wallet-transactions.json`: Raw transaction-level JSON file.

### 📤 Output
- `wallet_credit_scores.csv`: CSV file with wallet addresses and their credit scores.

| Wallet Address                                | Credit Score |
|-----------------------------------------------|--------------|
| 0x1234567890abcdef1234567890abcdef12345678    | 850          |
| 0xabcdefabcdefabcdefabcdefabcdefabcdefabcd    | 420          |

## 📖 Transparency
This system uses **rule-based scoring** for interpretability and extensibility. Future improvements can integrate machine learning models for advanced behavior detection.

## 📂 Repository Structure
- `wallet_credit_score.py`: Main scoring script.
- `user-wallet-transactions.json`: Sample transaction data.
- `wallet_credit_scores.csv`: Example output.
- `README.md`: Documentation.

---

© 2025 DeFi Analytics Lab
