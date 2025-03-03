#creates a histogram of the signifivant hits

import pandas as pd
import matplotlib.pyplot as plt


input_file = "/data/Summary Statistics/filtered_with_significant_hits.csv"
df = pd.read_csv(input_file)

plt.figure(figsize=(8, 6))
plt.hist(df["num_significant_pvalues"], bins=20, edgecolor='black')
plt.xlabel("Anzahl signifikanter Hits pro Phänotyp")
plt.ylabel("Häufigkeit (Anzahl Phänotypen)")
plt.title("Histogramm der Anzahl signifikanter Hits")
plt.grid(axis="y", linestyle="--", alpha=0.7)


output_image = "/data/Summary Statistics/histogram_significant_hits.png"
plt.savefig(output_image)

plt.show()
