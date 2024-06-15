import pandas as pd
import matplotlib.pyplot as plt

# Load the RDF data from the CSV file
rdf_df = pd.read_csv('./rdf_results.csv')

# Extract the distance values
distances = rdf_df['Distance']

# Plot RDF profiles
plt.figure(figsize=(12, 8))

# Identify same element pairs and different element pairs
for column in rdf_df.columns[1:]:
    elements = column.split('-')
    if elements[0] == elements[1]:  # Same element pairs
        plt.plot(distances, rdf_df[column], label=column, linestyle='-')
    else:  # Different element pairs
        plt.plot(distances, rdf_df[column], label=column, linestyle='--')

plt.xlabel('Distance')
plt.ylabel('g(r)')
#plt.title('Radial Distribution Function (RDF) Profiles')
plt.legend(title='Element Pair')
#plt.grid(True)
plt.savefig("RDF.png", dpi=600)
#plt.show()
