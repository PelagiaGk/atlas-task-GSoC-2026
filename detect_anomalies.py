import pandas as pd
import matplotlib.pyplot as plt

#Load data
try:
    df = pd.read_csv('anomaly.txt', sep=r'\s+', engine='python')
except FileNotFoundError:
    print("Error: anomaly.txt not found. Did you run the prmon commands?")
    exit()

# How many standard deviations each point is from the mean
mean_pss = df['pss'].mean()
std_pss = df['pss'].std()

df['z_score'] = (df['pss'] - mean_pss) / std_pss

# Anything > 2 standard deviations as an anomaly 
threshold = 2
df['is_anomaly'] = df['z_score'].abs() > threshold

# Visualization
plt.figure(figsize=(12, 6))
plt.plot(df['Time'], df['pss'], label='Memory (PSS)', color='blue', alpha=0.7)

#   Anomalies as red dots
anomalies = df[df['is_anomaly']]
plt.scatter(anomalies['Time'], anomalies['pss'], color='red', label='Anomaly Detected')

plt.title('prmon Memory Monitoring: Anomaly Detection (Z-Score)')
plt.xlabel('Time (seconds)')
plt.ylabel('Memory Usage (KB)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)

# Result
plt.savefig('detection_results.png')
print("Analysis complete! Check detection_results.png for the graph.")
plt.show()