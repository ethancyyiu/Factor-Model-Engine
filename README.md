# Factor-Model-Engine

# Factor Model Engine — Built From Scratch (by a First‑Year Student)

Hi! I’m Ethan — I’m a first‑year student who got obsessed with quant finance and decided to build a full factor‑model engine completely from scratch. From raw prices → signals → portfolios → performance → regressions.

This project started as “I wonder how factor investing actually works?” and turned into a full research pipeline that I’m genuinely proud of.

---

## 🚀 What This Project Is

This repo is a **mini quant research platform** I built to understand how real factor models work under the hood. It includes:

- A **data layer** (price loader + returns)
- A **factor layer** (momentum, volatility, reversal, SMA distance)
- A **portfolio layer** (long/short, z‑score weighted, composite)
- A **backtesting layer** (cumulative returns, Sharpe, comparisons)
- A **regression layer** (alpha, beta, t‑stats, R²)

Everything is coded by me — a first‑year student — but structured like a real quant research workflow.

---

## 🧠 Why This Project Matters

Most student projects stop at “plot some prices.”  
I wanted to go deeper and actually understand:

- how factors are constructed  
- how signals turn into weights  
- how long/short portfolios behave  
- how to evaluate a strategy properly  
- how to measure alpha and beta using regressions  

Even though this version uses **price‑only factors**, the architecture is the same one used in real quant shops. 

This version proves I understand the *process*, not just the data.

---

## 📊 Factors Implemented (Price‑Only Version)

I implemented four classic price‑based factors:

- **Momentum (12‑1)**  
  Stocks that performed well over the past year tend to keep performing well.

- **Volatility (21‑day)**  
  Measures how “jumpy” a stock is. Lower volatility often outperforms.

- **Reversal (5‑day)**  
  Short‑term moves often mean‑revert.

- **SMA Distance (20‑day)**  
  Captures trend strength relative to a moving average.

Each factor is normalized using **cross‑sectional z‑scores**, which lets me compare signals across stocks on the same day.

I also built a **composite factor** by combining all z‑scored signals.

---

## 📈 Portfolio Construction

I implemented three portfolio styles:

### 1. **Long/Short (Quantile‑Based)**
- Long top 20% of stocks  
- Short bottom 20%  
- Equal weight within each side  
- Dollar‑neutral  

### 2. **Z‑Score Weighted**
- Stronger signals → bigger weights  
- Smooth, continuous exposure  

### 3. **Composite Factor Portfolio**
- Combine all factors  
- Z‑score weight the final signal  
- This is the “main” strategy I analyze

---

## 🔍 Backtesting

I built a full backtest pipeline:

- daily portfolio returns  
- cumulative return curves  
- Sharpe ratios  
- strategy comparisons  
- summary tables  

This is where the strategy becomes real — not just math.

---

## 📉 Regression Analysis (Alpha, Beta, R²)

To understand what the strategy is actually doing, I ran OLS regressions of portfolio returns vs SPY:

- **alpha (annualized)** → excess return not explained by the market  
- **beta** → market exposure  
- **t‑stats** → statistical significance  
- **R²** → how much of the strategy the market explains  

This helped me answer questions like:

- “Is my strategy secretly just a market bet?”  
- “Does it have real alpha?”  
- “How stable is its exposure?”  

This is the part that made the project feel like real quant research.

---

## 📁 Project Structure

