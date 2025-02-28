#skript lädt den output des ersten Skriptes
#liest die jeweilige y_ID aus, und lädt die p_value.txt in CORID results ordnern
# inhalt der 3. Spalte (perm threshold 5%) und diskriminiert die p_values dagegen
# fügt die anzahl der signifikanten Werte in die 6. Spalte ein 

import os
import pandas as pd

def add_significant_pvalues(base_dir, input_csv, output_csv):
    df = pd.read_csv(input_csv) # input des ersten Skriptes laden 
    df["num_significant_pvalues"] = 0 # neue spalte inzufügen
#loop
    for index, row in df.iterrows():
        y_id = row["y_ID"]
        perm_threshold = row["perm_5"]        
#laden der p values mit der enstprechenden y_id
        folder_name = f"CORID_filtered_{y_id}"
        p_values_file = os.path.join(base_dir, folder_name, "p_values_phenotype_value.csv")
        p_values_df = pd.read_csv(p_values_file)
# vergleichen der p_values mit dem Threshold und sum erstellen 
        significant_count = (p_values_df["p_value"] < perm_threshold).sum()
# sum in die 6. Spalte einfügen 
        df.at[index, "num_significant_pvalues"] = significant_count
# speichern 
    df.to_csv(output_csv, index=False)

base_dir = "/data/results"
input_csv = "results/Summary Statistics/first_five_columns.csv"
output_csv = "results/Summary Statistics/finished_summary_statistics.csv"
add_significant_pvalues(base_dir, input_csv, output_csv)
