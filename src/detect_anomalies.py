import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

# 1. Load data
try:
    df = pd.read_csv('data/anomaly.txt', sep=r'\s+', engine='python')
except FileNotFoundError:
    print("Error: anomaly.txt not found. Did you run the prmon commands?")
    exit()

# Z-Score
mean_pss = df['pss'].mean()
std_pss = df['pss'].std()
df['z_score'] = (df['pss'] - mean_pss) / std_pss

df['is_anomaly_z'] = df['z_score'].abs() > 2

# Isolation Forest 
scaler = StandardScaler()
pss_scaled = scaler.fit_transform(df[['pss']])

# contamination=0.05 assumes roughly 5% of data is anomalous
model = IsolationForest(contamination=0.05, random_state=42)
df['is_anomaly_ml'] = model.fit_predict(pss_scaled)
# Convert ML output (-1 for anomaly, 1 for normal) to boolean
df['is_anomaly_ml'] = df['is_anomaly_ml'] == -1

# Visualization
plt.figure(figsize=(14, 7))
plt.plot(df['Time'], df['pss'], label='Memory (PSS)', color='gray', alpha=0.4, linestyle='--')

# Plot Z-Score Anomalies
z_anomalies = df[df['is_anomaly_z']]
plt.scatter(z_anomalies['Time'], z_anomalies['pss'], color='red', 
            label='Z-Score Anomaly', marker='x', s=50)

# Plot Isolation Forest Anomalies
ml_anomalies = df[df['is_anomaly_ml']]
plt.scatter(ml_anomalies['Time'], ml_anomalies['pss'], color='green', 
            label='Isolation Forest Anomaly', facecolors='none', edgecolors='green', s=100)

plt.title('prmon Memory Monitoring: Statistical vs. ML Anomaly Detection')
plt.xlabel('Time (seconds)')
plt.ylabel('Memory Usage (KB)')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)

# Save
plt.savefig('plots/detection_results.png')
print("Analysis complete!")
print(f"Z-Score detected: {len(z_anomalies)} points.")
print(f"Isolation Forest detected: {len(ml_anomalies)} points.")
plt.show()
