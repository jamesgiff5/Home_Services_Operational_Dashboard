# Home Services Operational Dashboard

Before becoming a Data Analyst, I ran my own exterior cleaning company in Orlando, FL. We specialized in pressure washing, soft washing, and paver sealing. I always wished I had better data to guide decisions, so I built the dataset I never had. This project uses synthetic data modeled directly on my real-world experience, scaled up in volume to uncover trends and evaluate performance with the kind of depth I used to want as a small business owner.

📊 [Excel Dashboard](./home_services_project.xlsx)

![Excel Dashboard Overview](assets/dashboard_preview.gif)

## 🧠 Executive Summary

Built on synthetic data modeled from my own business, this project uncovers key insights into how a small home services company operates in real life—in terms of volume, profitability, and customer behavior:

- **Consistent Volume:** ~90 jobs/month across two years, reflecting sustainable operations.
- **Bundling Wins:** Jobs with 3–4 services delivered 40–90% more profit per job.
- **Top Services:** Roof Cleaning and Paver Sealing dominate profit and revenue.
- **Healthy Margins:** Most services yield 80%+ profit margins, even when bundled.
- **Customer Trends:** 30% repeat client rate and 41% multi-service booking rate.

## 🔧 Dataset Creation

Using Python (in VS Code), with help from ChatGPT, I built a data generator powered by `Faker` and `NumPy` that reflects real-world dynamics from my days running an exterior-cleaning business: seasonal demand, ZIP-level pricing tiers (High, Mid, Standard), frequent bundling, and even repeat client behavior.  
🛠️ [Data Generation Script](./data_generation/generate_dataset.py)  
📂 [Data Folder](./data/)  

<img src="assets/entity_relationship_diagram.png" width="600"/>

## 💡 Key Business Questions Answered

- Which services drive the most profit and why?
- How do bundled jobs compare to single-service bookings?
- Are we operating near job capacity across months?
- What’s the ratio of repeat clients and multi-service customers?
- How do profit margins shift with seasonal demand?


## 📊 Analysis Summary

### 1. **Operational Efficiency and Growth Over Time**

- Job volume remained steady between the two years, with 531 jobs completed in 2023 and 551 in 2024. This reflects strong operational consistency in a seasonal and demand-driven industry. Monthly job completion averaged around 90, suggesting the business operated near capacity without frequent overloading.

- The rolling 7‑day average, plotted alongside a 3-jobs-per-day ceiling, confirmed that even during busier months, job load stayed within manageable limits. This supports a realistic model for small teams and lean operations.

### 2. **Revenue and Profit by Service Type**

- Paver Sealing brought in the highest average ticket at around $1,800 per job, though it maintained slimmer profit margins at roughly 60%. Roof Cleaning, by comparison, averaged $1,150 per job but held a strong 81% profit margin, making it the most valuable blend of volume and profitability.

- Other service types, such as Window Cleaning and Driveway Cleaning, clustered in the $80 to $320 range, all maintaining healthy margins as well. This consistency indicates good cost control and pricing strategy across service lines.

    ![Profitability By Service Type Table](assets/profitability_by_service_type.png)

### 3. **Bundling Strategy Impact**

- Jobs with multiple services consistently produced higher total profit. Single-service jobs averaged $559 in profit, while bundling four services pushed the average to $1,068.

- Although total job cost rose slightly with more services, profit margins remained stable around 80%, suggesting bundling boosts efficiency without hurting profitability.

- Interestingly, average job cost was actually higher for single-service jobs. This is due to high-ticket services like paver sealing and roof cleaning often being booked alone. These services carry higher costs, but their strong margins keep them highly profitable. When smaller, lower-cost services are bundled, margins improve and total profits climb — highlighting the value of cross-service packaging. 

    ![Bundling Vs Profit Table](assets/how_bundling_multiple_services_affects_profit.png)

### 4. **Seasonality and Scheduling Patterns**

- Spring months like April and May showed the highest job volume, with a summer taper and a secondary spike around the holiday season. This pattern aligns with observed demand trends in Florida-based operations, where winter weather doesn’t constrain year-end service work.

- Despite the seasonal demand, job load never breached the daily capacity threshold, showing that scheduling remained controlled and sustainable across the year.

### 5. **Customer Behavior and Retention**

- Roughly 30% of bookings came from repeat clients, a healthy figure with potential for improvement through retention efforts and loyalty campaigns.

- About 41% of all jobs involved multiple services. Although discounted when bundled, these upsells still boosted total profitability. With healthy margins holding steady, bundling proved to be a strategic advantage, especially when promoted during high-demand months.

## 🎯 Conclusion & Key Takeaways

Building this dashboard helped confirm a few things that align with what I saw in the field:

- **Consistency matters.** Steady job volume and capacity awareness kept the business sustainable through seasonal demand.
- **Upselling works.** Bundled services increased profit without harming margins, showing how smart packaging can maximize value.
- **Profit comes from focus.** Roof cleaning and paver sealing drove the most revenue and should stay at the center of strategy.
- **Customer behavior tells a story.** With 30% of clients returning and 41% choosing bundled services, there's clear room to grow through retention and loyalty.
- **Synthetic doesn't mean random.** Modeling based on personal experience led to insights that feel grounded and usable, not generic.

Overall, this kind of structured analysis makes it easier to spot what’s working, what’s not, and where to focus next. It’s the kind of clarity I always wished I had when I was running the show solo and wearing every hat.

## ⚠️ Caveats & Limitations

- The dataset is synthetic (not real business data) so although it follows realistic patterns, it’s not a perfect mirror of a live operation.
- It assumes jobs happen any day of the week, but in reality your business probably had weekends, holidays, or downtime.
- Calculated costs cover only direct cost of goods (cleaning supplies, sealer, etc.). They don’t include labor, travel, marketing, equipment, insurance or other overheads.
- Profit margins look strong, but overlooking indirect expenses (like fuel, vehicle maintenance, or admin time) likely overstate actual net profit.
- The model doesn’t factor in cancellations, last-minute reschedules, or no-shows—which can impact real-world performance.
- There’s no seasonal pricing variation (like discounts in slow months or premiums in busy ones), and no account for price competition or local market saturation.

## 🧭 Opportunities for Further Exploration

This project didn’t cover everything in the dataset. Areas for future analysis could include:

- **Forecasting:** Build predictive models for future job demand.
- **Pricing Optimization:** Simulate discounts and bundle offers.
- **Customer Segmentation:** Cluster clients by value or behavior.
- **Satisfaction Trends:** Explore the impact of payment delays or review scores.