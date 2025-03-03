# this skript is used to call the enseml api to fetch the AGIDs of CHR:POS data for Y-sample with more than 10 significant hits
#Output is stored in the last column 

import pandas as pd
import requests
import os
import time

# input output dirs
input_dir = "/data/Y_IDs_with_num_sign_>10/"
output_dir = "/data/Summary Statistics/for_GO_enrichment/"

# Abfrage der Ensembl REST API
def get_agi_id(chromosome, position):
    url = f"https://rest.ensembl.org/overlap/region/arabidopsis_thaliana/{chromosome}:{position}-{position}?feature=gene;content-type=application/json"
    response = requests.get(url, headers={"Content-Type": "application/json"})

    if response.status_code == 200:
        data = response.json()
        print(f"API-Antwort für {chromosome}:{position} -> {data}")  # Debugging-Ausgabe, kann auch weggelassen werden, ist aber ganz coole info.
        if isinstance(data, list) and len(data) > 0:  
            return data[0].get("id", "NA") 
    else:
        print(f"Fehlerhafte API-Antwort ({response.status_code}) für {chromosome}:{position}")
    
    return "NA" 


# loop zur verarbeitung
for filename in os.listdir(input_dir):
    if filename.endswith("_significant_snps.csv"):
        y_id = filename.split("_")[0]  
        input_file = os.path.join(input_dir, filename)
        output_file = os.path.join(output_dir, f"{y_id}_summary_AGID_>10hits.csv")
# input datei Datei
        df = pd.read_csv(input_file)
#  AGI-IDs hinzufügen in neue Spalte 
        df["AGI_ID"] = df.apply(lambda row: get_agi_id(int(row["CHR"]), int(row["POS"])), axis=1)
# Speichern
        df.to_csv(output_file, index=False)
        print(f"Erstellt: {output_file}")
# 1 Sekunde Pause nach jeder Date i
        time.sleep(1)

