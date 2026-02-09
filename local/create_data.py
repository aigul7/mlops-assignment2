"""
Generate athletes.csv dataset for Assignment 2
"""
import pandas as pd
import numpy as np

np.random.seed(42)
n = 1000

data = {
    'athlete_id': range(1, n + 1),
    'name': [f'Athlete_{i}' for i in range(1, n + 1)],
    'age': np.random.randint(18, 40, n),
    'height': np.random.normal(175, 10, n),
    'weight': np.random.normal(75, 12, n),
    'country': np.random.choice(['USA', 'China', 'Russia', 'Germany', 'UK', 'France', 'Japan', 'Australia'], n),
    'sport': np.random.choice(['Swimming', 'Athletics', 'Gymnastics', 'Cycling', 'Rowing'], n),
    'years_experience': np.random.randint(1, 20, n),
    'training_hours_per_week': np.random.randint(10, 40, n),
}

df = pd.DataFrame(data)

# Target variable: 45% win medals
medals = ['Gold'] * 100 + ['Silver'] * 150 + ['Bronze'] * 200 + ['None'] * 550
np.random.shuffle(medals)
df['medal'] = medals

df.to_csv('athletes.csv', index=False)

print(f" Created: {len(df)} athletes")
print(f"\n Medal distribution:")
print(df['medal'].value_counts())
