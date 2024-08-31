individuals_file = open('Individuals.txt', 'r')
header_line = individuals_file.readline()
# Split the header line into an array of column names
column_names = header_line.strip().split('\t')
# Create two empty lists for the two columns
ID   = []
SYMM = []

# Read the data lines
for line in individuals_file:
  line = line.strip()
  if not line:
    continue
  values = line.split()
  ID.append(values[0])
  SYMM.append(values[1])

individuals_file.close()
import os
for i in range(len(ID)):
  source_path = os.path.join('/data/Mg_Ni_V/STRUCTURE_PREDICTION/Mg_Ni_V/post_processing/BONDS_SORTED', f'{i+1}')
  #destination_path = f"/content/BONDS_SORTED/BOND_LENGTH/SYMM_[i]
  destination_path = f"/data/Mg_Ni_V/STRUCTURE_PREDICTION/Mg_Ni_V/post_processing/BOND_LENGTH/SYMM_{SYMM[i]}/{i+1}"
  # Check if the source file exists
  if os.path.exists(source_path):
    # Copy the file
    !cp "{source_path}" "{destination_path}"
  else:
    print(f"File not found: {source_path}")
