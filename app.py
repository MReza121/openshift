import pandas as pd
import os

# Define the path where the PVC is mounted
pvc_mount_path = '/etc/myapp'


# Sample data to be saved to CSV
data = {
    'Column1': [1, 2, 3],
    'Column2': ['A', 'B', 'C']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Define the CSV file path within the PVC mount
csv_file_path = os.path.join(pvc_mount_path, 'data.csv')

# Save the DataFrame to CSV
df.to_csv(csv_file_path, index=False)

print(f"CSV file saved to {csv_file_path}")
