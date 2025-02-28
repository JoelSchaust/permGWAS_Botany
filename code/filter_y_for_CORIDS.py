#vermutung: Der Fehler war wahrscheinlich dass der index bei pandas automatisch mit gespeichert wurd.
#kam dann im Output in die erste Spalte, was dann natürlich mit permGWAS nicht funzt. 
#Hier wird dann einfach spalte 2 und 3 behalten (index 1 und 2) und gespeichert. 


import os
import pandas as pd

# Pfade
cor_file = "/data/Cor.csv"
y_folder = "/data/ARAPHENO/"
temp_folder = "/data/y_filtered_for_CORidsv2/"

# Cor.csv laden idsspeicher
df_k = pd.read_csv(cor_file, index_col=0)
sample_ids_k = set(df_k.index.astype(str))

# Loop 
for y_file in os.listdir(y_folder):
    if y_file.endswith(".csv"):
        y_path = os.path.join(y_folder, y_file)
        df_y = pd.read_csv(y_path)        
        df_y["accession_id"] = df_y["accession_id"].astype(str)  # IDs als Strings nnur die in K existieren
        df_y_filtered = df_y[df_y["accession_id"].isin(sample_ids_k)]
# HIER WIRD DANN NUR SPALTE 2 und 3 BEHALTEN!!!!
        if df_y_filtered.shape[1] > 2:
            df_y_filtered = df_y_filtered.iloc[:, [1, 2]]  # Nur die ersten zwei Spalten behalten
# Saving
        filtered_y_path = os.path.join(temp_folder, f"CORID_filtered_{y_file}")
        df_y_filtered.to_csv(filtered_y_path, index=False)

