"""
This script creates a synthetic dataset simulating a residential home services business.
It generates four CSV files: jobs.csv, services.csv, clients.csv, and zip_regions.csv.

HOW TO RUN:
1. Make sure you have Python 3 installed.
2. Install required packages using:
   pip install faker numpy pandas
3. Run the script in your terminal or VS Code:
   python generate_dataset.py
4. Output CSV files will be saved in the 'data' directory.

Note: The data is randomized but based on real-world logic and business operations.
"""

# Synthetic Home Services Dataset Generator
import pandas as pd
import numpy as np
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()
np.random.seed(42)

# ---- Constants ----
ZIP_TIERS = {
    '34786': 'High', '32836': 'High', '32789': 'High', '32792': 'High', '32779': 'High',
    '32746': 'Mid', '32750': 'Mid', '32714': 'Mid',
    '32808': 'Standard', '32825': 'Standard', '32707': 'Standard', '32765': 'Standard'
}
ZIP_CODES = list(ZIP_TIERS.keys())
SERVICES = [
    'House Wash', 'Roof Cleaning', 'Driveway Cleaning', 'Patio/Pool Deck Cleaning',
    'Window Cleaning', 'Paver Sealing', 'Gutter Cleaning',
    'Solar Panel Cleaning', 'Pool Screen Cleaning'
]

SERVICE_WEIGHTS = {
    'Roof Cleaning': 0.2,
    'Paver Sealing': 0.1,
    'House Wash': 0.15,
    'Driveway Cleaning': 0.1,
    'Patio/Pool Deck Cleaning': 0.1,
    'Window Cleaning': 0.15,
    'Gutter Cleaning': 0.1,
    'Solar Panel Cleaning': 0.1,
    'Pool Screen Cleaning': 0.1
}

PAYMENT_METHODS = {
    'High': ['Check', 'Card', 'Zelle', 'Cash'],
    'Mid': ['Card', 'Zelle', 'Check', 'Cash'],
    'Standard': ['Card', 'Zelle', 'Cash', 'Check']
}
PAYMENT_WEIGHTS = {
    'High': [0.4, 0.4, 0.1, 0.1],
    'Mid': [0.15, 0.55, 0.25, 0.05],
    'Standard': [0.05, 0.6, 0.3, 0.05]
}

MONTH_WEIGHTS = {
    1: 0.8, 2: 0.9, 3: 1.1, 4: 1.5, 5: 1.3, 6: 1.1,
    7: 1.2, 8: 0.7, 9: 0.9, 10: 1.1, 11: 1.3, 12: 1.2
}

# ---- Helper Functions ----
def generate_client(client_id):
    zip_code = random.choice(ZIP_CODES)
    return {
        'client_id': client_id,
        'client_name': fake.name(),
        'zip_code': zip_code,
        'region_tier': ZIP_TIERS[zip_code]
    }

def round_to_five(n):
    return int(round(n / 5.0) * 5)

def generate_services(job_id, zip_code):
    tier = ZIP_TIERS[zip_code]
    num_services = 1 if random.random() > 0.6 else random.randint(2, 4)
    selected = random.choices(SERVICES, weights=[SERVICE_WEIGHTS[s] for s in SERVICES], k=num_services)
    selected = list(dict.fromkeys(selected))

    if 'Paver Sealing' in selected and len(selected) > 1:
        selected = ['Paver Sealing']
        num_services = 1

    services = []
    for idx, s in enumerate(selected):
        discount_multiplier = 1.0
        if idx > 0 and s not in ['Paver Sealing', 'Roof Cleaning']:
            discount_multiplier = 0.8

        if s == 'Roof Cleaning':
            base_price = max(np.random.normal(loc=1100, scale=500), 500)
        elif s == 'Paver Sealing':
            base_price = max(np.random.normal(loc=1600, scale=800), 900)
        elif s == 'Window Cleaning':
            base_price = np.random.uniform(50, 125)
        elif s == 'Driveway Cleaning' and num_services == 1:
            base_price = 225
        elif s == 'Driveway Cleaning':
            base_price = np.random.uniform(100, 175)
        elif s == 'Pool Screen Cleaning':
            base_price = max(np.random.uniform(275, 400), 275)
        elif s == 'House Wash':
            base_price = max(np.random.uniform(200, 300), 225)
        elif s == 'Patio/Pool Deck Cleaning':
            base_price = np.random.uniform(100, 200)
        else:
            base_price = np.random.uniform(80, 175)

        adjusted_price = base_price * discount_multiplier
        price = round_to_five(adjusted_price * (1.1 if tier == 'High' else 1))

        if s == 'Paver Sealing':
            cost = max(round_to_five(price * 0.4), 325)
        else:
            cost = round_to_five(price * np.random.uniform(0.1, 0.3))

        services.append({'job_id': job_id, 'service_type': s, 'price': price, 'cost': cost})
    return services

# ---- Data Generation ----
clients = []
jobs = []
services = []
client_dict = {}

start_date = datetime(2023, 1, 1)
end_date = datetime(2024, 12, 31)
date_range = pd.date_range(start=start_date, end=end_date).to_list()

job_id = 1
client_id = 1

for d in date_range:
    jobs_today = np.random.poisson(1.5 * MONTH_WEIGHTS[d.month])
    for _ in range(min(jobs_today, 3)):
        if random.random() < 0.8:
            if client_id not in client_dict:
                c = generate_client(client_id)
                client_dict[client_id] = c
                clients.append(c)
                client_id += 1
        else:
            if len(client_dict) == 0:
                c = generate_client(client_id)
                client_dict[client_id] = c
                clients.append(c)
                client_id += 1

        cid = random.choice(list(client_dict.keys()))
        zip_code = client_dict[cid]['zip_code']

        job_services = generate_services(job_id, zip_code)
        total_price = sum(s['price'] for s in job_services)
        total_cost = sum(s['cost'] for s in job_services)
        duration = 2 if any(s['service_type'] == 'Paver Sealing' for s in job_services) else 1
        tier = ZIP_TIERS[zip_code]

        method = random.choices(PAYMENT_METHODS[tier], weights=PAYMENT_WEIGHTS[tier])[0]
        status = 'Paid'
        delay = 0 if random.random() > 0.1 else 1
        score = random.choices([5, 4, 3, 2, 1], weights=[0.7, 0.2, 0.05, 0.03, 0.02])[0]

        jobs.append({
            'job_id': job_id,
            'job_date': d.date(),
            'client_id': cid,
            'zip_code': zip_code,
            'total_price': total_price,
            'total_cost': total_cost,
            'duration_days': duration,
            'payment_status': status,
            'payment_method': method,
            'payment_delay_days': delay,
            'review_score': score,
            'num_services': len(job_services)
        })

        for s in job_services:
            s['service_id'] = f"S{job_id}_{s['service_type'][:3]}"
            services.append(s)

        job_id += 1

zip_regions = [{'zip_code': z, 'region_name': fake.city(), 'tier': ZIP_TIERS[z]} for z in ZIP_CODES]

# ---- Export ----
jobs_df = pd.DataFrame(jobs)
services_df = pd.DataFrame(services)
clients_df = pd.DataFrame(clients)
zip_regions_df = pd.DataFrame(zip_regions)

jobs_df.to_csv("jobs.csv", index=False)
services_df.to_csv("services.csv", index=False)
clients_df.to_csv("clients.csv", index=False)
zip_regions_df.to_csv("zip_regions.csv", index=False)
