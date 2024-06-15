import warnings
warnings.filterwarnings('ignore', message='.*OVITO.*PyPI')
from ovito.io import import_file
from ovito.modifiers import CoordinationAnalysisModifier
import pandas as pd
# Load input data.
pipeline = import_file("input.data") #example data file 

# Print the list of input particle types.
# They are represented by ParticleType objects attached to the 'Particle Type' particle property.
#for t in pipeline.compute().particles.particle_types.types:
#    print("Type %i: %s" % (t.id, t.name))

# Calculate partial RDFs:
pipeline.modifiers.append(CoordinationAnalysisModifier(cutoff=5.0, number_of_bins=100, partial=True))
#
## Access the output DataTable:
rdf_table = pipeline.compute().tables['coordination-rdf']
#
## The y-property of the data points of the DataTable is now a vectorial property.
## Each vector component represents one partial RDF.
rdf_names = rdf_table.y.component_names
#
## Print a list of partial g(r) functions.
#for component, name in enumerate(rdf_names):
#    print (component, name)
#    print("g(r) for pair-wise type combination %s:" % name)
#    print(rdf_table.y[:,component])
#
## The DataTable.xy() method yields everthing as one combined NumPy table.
## This includes the 'r' values in the first array column, followed by the
## tabulated g(r) partial functions in the remaining columns. 
#print(rdf_table.xy())
# Create column names for the DataFrame
columns = ['Distance'] + [f'{name}' for name in rdf_names]
## Convert the list of dictionaries to a DataFrame
rdf_df = pd.DataFrame(rdf_table.xy(),columns=columns)
#
## Step 4: Export the RDF data to a CSV file
rdf_df.to_csv("rdf_results.csv", index=False)