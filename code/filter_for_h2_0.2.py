import pandas as pd

input_file = "/Summary Statistics/finished_summary_statistics.csv"
output_file = "/Summary Statistics/h2filtered_summary_statistics.csv"


df = pd.read_csv(input_file)
filtered_df = df[df["narrow_sense"] > 0.2]

filtered_df.to_csv(output_file, index=False)


