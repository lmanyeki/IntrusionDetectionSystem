import pandas as pd

def rules_based_detection(dataframe):
    results = []

    for _, row in dataframe.iterrows():
        if row['src_bytes'] > 1000:  # Example Rule 1: Large packet size
            results.append("Potential Threat: High Traffic")
        elif row['protocol_type'] == 'icmp':  # Example Rule 2: ICMP Flooding
            results.append("Potential Threat: ICMP Flood")
        else:
            results.append("Safe")

    dataframe['Analysis Result'] = results
    return dataframe

# Example usage
data = {
    'src_bytes': [500, 1500, 700, 2000],
    'protocol_type': ['tcp', 'tcp', 'icmp', 'udp']
}
df = pd.DataFrame(data)
result_df = rules_based_detection(df)
print(result_df)
