
import json
import sys
import pandas as pd
from datetime import datetime

def calculate_score(features):
    # Rule-based scoring logic
    score = 500  # Start from midpoint

    # Deposit to borrow ratio
    if features['total_borrow'] > 0:
        deposit_borrow_ratio = features['total_deposit'] / features['total_borrow']
        if deposit_borrow_ratio >= 2:
            score += 200
        elif deposit_borrow_ratio >= 1:
            score += 100
        else:
            score -= 100
    else:
        score += 150  # No borrow is safer

    # Repayment ratio
    if features['total_borrow'] > 0:
        repay_ratio = features['total_repay'] / features['total_borrow']
        if repay_ratio >= 1:
            score += 200  # Fully repaid
        else:
            score += int(200 * repay_ratio)
    else:
        score += 50

    # Liquidations (penalty)
    score -= features['liquidation_count'] * 100

    # Activity duration (reward longer activity)
    duration_days = features['active_duration_days']
    if duration_days >= 180:
        score += 100
    elif duration_days >= 90:
        score += 50
    else:
        score -= 50

    # Transaction count (filter out bots with too few txns)
    if features['transaction_count'] < 3:
        score -= 200

    # Clamp score to 0–1000
    return max(0, min(1000, score))

def process_transactions(json_file, output_file):
    with open(json_file, 'r') as f:
        data = json.load(f)

    df = pd.DataFrame(data)

    # Parse timestamps
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')

    # Aggregate per wallet
    wallet_groups = df.groupby('userWallet')

    wallet_scores = []
    for wallet, group in wallet_groups:
        total_deposit = group[group['action'] == 'deposit']['actionData'].apply(lambda x: float(x['amount'])).sum()
        total_borrow = group[group['action'] == 'borrow']['actionData'].apply(lambda x: float(x['amount'])).sum()
        total_repay = group[group['action'] == 'repay']['actionData'].apply(lambda x: float(x['amount'])).sum()
        liquidation_count = group[group['action'] == 'liquidationcall'].shape[0]
        transaction_count = group.shape[0]

        active_duration_days = (group['timestamp'].max() - group['timestamp'].min()).days

        features = {
            'total_deposit': total_deposit,
            'total_borrow': total_borrow,
            'total_repay': total_repay,
            'liquidation_count': liquidation_count,
            'transaction_count': transaction_count,
            'active_duration_days': active_duration_days
        }

        score = calculate_score(features)

        wallet_scores.append({
            'wallet': wallet,
            'credit_score': score
        })

    # Save to CSV
    pd.DataFrame(wallet_scores).to_csv(output_file, index=False)
    print(f"Wallet credit scores saved to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python wallet_credit_score.py <input_json_file> <output_csv_file>")
    else:
        process_transactions(sys.argv[1], sys.argv[2])
