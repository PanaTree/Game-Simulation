# Multi-Regional Supply Chain Strategic Simulator

## 📌 Project Overview
Developed as a strategic decision-support tool for the **SUTD Supply Chain Management (40.260)** simulation game. This engine models a complex, multi-continental supply chain to optimize cash flow, inventory levels, and production capacity.

## 🚀 Key Features
* **Stochastic Demand Modeling:** Implements Gaussian distribution and trigonometric seasonal curves to simulate market volatility across 5 distinct regions (Calopeia, Sorange, etc.).
* **Production & Inventory Logic:** Simulates factory upgrades, lead times, transit delays, and daily holding costs.
* **Monte Carlo Analysis:** Supports running N-iterations to determine the statistical probability of success for specific Reorder Point (ROP) and Order Quantity (OQ) policies.
* **Financial Tracking:** Real-time monitoring of cash balances, including daily interest accumulation and upfront capital expenditures (CAPEX).

## 🛠️ Technical Stack
* **Python 3.x**
* **Pandas:** For demand data ingestion and historical tracking.
* **Matplotlib:** For visualizing inventory cycles, production peaks, and stockout periods.
* **NumPy/Math:** For modeling seasonal demand curves and financial compounding.

## 📊 Sample Output
The simulator generates 4-tier visual analytics covering:
1. **Cash Balance** (Liquidity tracking)
2. **Inventory Levels** (Per region)
3. **Production Progress** (Factory utilization)
4. **Stockout Analysis** (Identifying supply-chain bottlenecks)

## 💡 Engineering Takeaway
This project demonstrates the use of **Systems Thinking** to solve operational challenges, moving beyond static spreadsheets to dynamic, code-based simulations that account for lead-time variability and capital constraints.