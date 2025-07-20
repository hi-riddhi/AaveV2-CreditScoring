# analysis.md
## Wallet Credit Score Distribution & Behavioral Insights
### 1. Score Distribution Overview
After processing and scoring all wallets from the Aave V2 transaction dataset, the resulting credit scores were binned into ten equal-width ranges from 0 to 999. The distribution helps reveal overall risk trends and outlier clusters within the protocol.

Distribution of wallet counts across score bands (example data):

| Credit Score Range | Number of Wallets |
|--------------------|------------------|
| 0–99               | 99               |
| 100–199            | 90               |
| 200–299            | 96               |
| 300–399            | 127              |
| 400–499            | 85               |
| 500–599            | 95               |
| 600–699            | 90               |
| 700–799            | 93               |
| 800–899            | 92               |
| 900–999            | 132              |

#### Score Distribution Histogram

The plot below visualizes the number of wallets in each credit score range:
### 2. Behavioral Analysis by Score Range
#### A. **Low Score Ranges (0–299)**

- **Common Behavior:**  
  - Frequent liquidations and very poor or negligible repayments.
  - Large gaps between borrowed and repaid amounts.
  - Many wallets show very short activity spans, low transaction counts, or appear abandoned after risk events.
- **Interpretation:**  
  - These accounts are high risk, often failing to fulfill obligations. May include bots, exploit attempts, or wallets engaged in speculative or risky protocol interactions.

#### B. **Mid Score Ranges (300–699)**

- **Common Behavior:**  
  - Periodic repayment and protocol engagement but with occasional missed obligations or liquidations.
  - Borrowing activity may approach or exceed deposits, indicating increased leverage or risk appetite.
  - Activity spans are mixed—some new or short-lived wallets, others with longer, moderate histories.
- **Interpretation:**  
  - Represents a "gray zone" of evolving behavior—risk is present, but there is evidence of attempted repayment or responsible use. Some wallets may be improving, while others are in decline.

#### C. **High Score Ranges (700–1000)**

- **Common Behavior:**  
  - Consistent full or excess repayments, low to zero liquidations, and positive deposit/borrow ratios.
  - Long active durations and high transaction counts, suggesting persistent protocol engagement.
  - Wallets routinely avoid risk events and participate in both depositing and borrowing in balanced fashion.
- **Interpretation:**  
  - These addresses exemplify responsible usage: proactive in meeting obligations, using borrowing prudently, and contributing to liquidity. They appear trustworthy and may make good candidates for further protocol rewards or partnership.

### 3. Summary Insights
- The credit scoring system effectively segments users by observable risk, highlighting pools of reliable participants and flagging behaviors associated with default or exploitation.
- The distribution is somewhat bimodal, with a significant portion of high-scoring users, but also many low scorers due to risky or automated wallet behavior.
- Most reliable users show repeated repayment habits, few if any liquidations, and maintain long, active protocol histories.
- The methodology and transparency in score driver selection ensure findings are actionable and open to further refinement.

**For full feature descriptions and model methodology, see `readme.md`. The input and processed output files are provided in this repository for reproducibility.**
