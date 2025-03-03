#skript 
import pandas as pd


input_file = "results/Summary Statistics/h2filtered_summary_statistics.csv"
output_file = "results/Summary Statistics/filtered_with_significant_hits.csv"

df = pd.read_csv(input_file)

df_significant = df[df["num_significant_pvalues"] > 0]

num_significant = df_significant.shape[0]

df_significant.to_csv(output_file, index=False)

