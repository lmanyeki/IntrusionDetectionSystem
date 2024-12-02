import pandas as pd
import random

# Define the number of rows for the dataset
NUM_ROWS = 1000

# Function to generate random network traffic data
def generate_random_data():
    data = []
    for _ in range(NUM_ROWS):
        row = {
            'Duration': random.randint(1, 300),  # Random duration in seconds
            'Protocol_Type': random.choice(['TCP', 'UDP', 'ICMP']),
            'Service': random.choice(['http', 'ftp', 'dns', 'smtp', 'telnet']),
            'Flag': random.choice(['SYN', 'ACK', 'RST', 'FIN']),
            'src_bytes': random.randint(50, 5000),  # Random bytes sent from source
            'dst_bytes': random.randint(50, 5000),  # Random bytes sent to destination
        }
        data.append(row)
    return data

# Function to label data based on conditions
def label_data(row):
    # Example conditions for labeling
    if row['src_bytes'] > 1000 and row['dst_bytes'] < 500:
        return 'attack'
    elif row['Protocol_Type'] == 'UDP' and row['Flag'] == 'SYN':
        return 'attack'
    else:
        return 'normal'

# Generate random data
random_data = generate_random_data()

# Create a DataFrame from the random data
df = pd.DataFrame(random_data)

# Apply the labeling function
df['Class'] = df.apply(label_data, axis=1)

# Save the generated and labeled data to a CSV file
output_file = 'generated_labeled_network_traffic.csv'
df.to_csv(output_file, index=False)

print(f"Randomly generated and labeled data saved to {output_file}")
