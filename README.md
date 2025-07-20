# 🦄 Aave V2 Wallet Credit Scoring — Quickstart Guide

Hey there, DeFi explorer!  
Welcome to this playful and powerful toolkit that gives every wallet on Aave V2 a credit score—between **0** (super risky 🛑) and **1000** (DeFi royalty 👑)—all based on on-chain behavior. Here’s everything you need to get started and see the protocol’s wallets in a whole new light.

## 🚀 What Does This Project Do?

- **Reads raw wallet activity (JSON) from Aave V2**
- **Crunches the numbers** to spot good (and not-so-good) protocol citizens
- **Gives every wallet a score**, so you can see at a glance who’s reliable, who’s risky, and who’s somewhere in between
- **Outputs a beautifully organized CSV** lots of features and friendly labels!

## 🛠️ Our Method, Distilled

We want a fun-but-fair way to judge a wallet’s DeFi contribution. That means:
- **Positive marks for:**
  - Big deposits 💰
  - Borrowing only what you can handle 🙌
  - Repaying what you owe (or even extra!) 🥇
  - Sticking around — activity over a long time 🌱
- **Negative marks for:**
  - Getting liquidated (ouch!) 🧨
  - Never paying back (not cool...) 🤨
  - Bot-like or “flash in the pan” usage 🤖

**We roll all these clues into a juicy credit score using a smart machine learning model.**

## 🏗️ Architecture & Processing Flow

Here’s the journey from raw data to super scores, step-by-step:

1. **Data Ingestion:**  
   We gulp up your Aave wallet transactions, straight from a JSON file.

2. **Feature Cooking:**  
   For each wallet, we whip up stats like “total deposited,” “total borrowed,” number of liquidations, ratio of repaid-to-borrowed, activity streak (in days), and more.

3. **Score Mastering:**  
   Every wallet gets run through the ML model, which weighs all their actions—the good, the bad, the ugly—and spits out a shiny credit score between 0 and 1000.

4. **User-Friendly CSV Output:**  
   Boom! You get a CSV file with wallet address, their score, behavior breakdown, and a little ‘risk category’ tag (Low / Medium / High).

## 📦 File Guide

- **wallet_credit_score.py** — The ~magic~ code!
- **user-wallet-transactions.json** — Your Aave data goes here.
- **wallet_credit_scores.csv** — The friendly, easy-to-read results.
- **analysis.md** — All the deep-dive stats, charts, and wallet behavior insights.
- **readme.md** — This file, with the answers to everything.

## 🔥 How To Run (It’s Easy!)

1. **Install dependencies:**
   ```
   pip install pandas xgboost scikit-learn
   ```

2. **Pop in your transaction file and run:**
   ```
   python wallet_credit_score.py user-wallet-transactions.json wallet_credit_scores.csv
   ```

That’s it!  
Check `wallet_credit_scores.csv` for friendly scores and wallet details you can actually use.

## ⚡️ Want More?

- **Customize features:** Try adding more stats! Maybe reward long-term liquidity, or penalize wild borrowing.
- **Plug in your own labels:** If you have real-world ‘good vs. bad’ outcomes, train the model even smarter!
- **Export new analysis:** The output CSV is perfect for dashboards, audits, or airdrop curation.

## 🎨 In a Nutshell

This tool turns messy on-chain chaos into clear, actionable credit insights—fast, flexible, and fun. It’s as transparent as possible, and completely extendable for Aave V2, your own protocol, or any EVM chain you love!

**Ready to score some wallets? Let’s DeFi! 🦄**


Built by your friendly DeFi toolkit developer, with a pinch of code and a dash of curiosity. Enjoy! ⭐️
