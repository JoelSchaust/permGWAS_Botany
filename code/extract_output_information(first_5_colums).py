#Skript extrahiert die ersten fünf Spalten due benötigt werden: yID, Narrow Sense, bonferroni 5%, perm 5%, num_indiv 

import os
import pandas as pd

def extract_summary_stats(base_dir, output_csv):
    data = [] #leer     
# Alle Alle subordner in denen die Ergebnisse liegen durchsuchen
    for folder in os.listdir(base_dir):
        folder_path = os.path.join(base_dir, folder)                # 
        if os.path.isdir(folder_path) and folder.startswith("CORID_filtered_Y"):
            y_id = folder.split("_")[-1]  # Y-ID extrahieren
            summary_file = os.path.join(folder_path, "summary_statistics_phenotype_value.txt")
            
# Prüfen, ob die Datei existiert (Da ja keine fortlaufenden yIDs -nur quality of life)
            if os.path.exists(summary_file):
                with open(summary_file, 'r') as f:
                    lines = f.readlines()                    
# Werte initialisiern ohne yID,da diese im Ordnernamen extrahiert wird
                narrow_sense = bonferroni_5 = perm_5 = num_individuals = None
# Loop über alle Zeilen des txt.
                for line in lines:
                    if "Narrow-sense heritability estimate:" in line:
                        narrow_sense = float(line.split("\t")[-1].strip())
                    elif "Bonferroni threshold (5% significance level):" in line:
                        bonferroni_5 = float(line.split("\t")[-1].strip())
                    elif "Permutation-based threshold (5% significance level):" in line:
                        perm_5 = float(line.split("\t")[-1].strip())
                    elif "Number of individuals:" in line:
                        num_individuals = int(line.split("\t")[-1].strip())
                
# Daten speichern in leeren Dataframe
                data.append([y_id, narrow_sense, bonferroni_5, perm_5, num_individuals])
    
# DataFrame erstellen
    df = pd.DataFrame(data, columns=["y_ID", "narrow_sense", "bonferroni_5", "perm_5", "num_individuals"])
    
# Savepath + savecsv 
    save_path = "/results/Summary Statistics/first_five_columns.csv"
    df.to_csv(save_path, index=False)

base_dir = "/results/"
output_csv = "summary_statistics_table.csv"
extract_summary_stats(base_dir, output_csv)