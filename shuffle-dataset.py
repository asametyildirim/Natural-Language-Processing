"""
If we want to mix your dataset, you can use the codes below
"""


import csv
import random

# Read CSV file
with open('sample_data/dogal-dil-isleme-dataset1.csv', newline='',encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    rows = list(reader)

# Shuffle lines
random.shuffle(rows)

# Write updated lines to CSV file
with open('sample_data/dogal-dil-isleme-dataset1.csv', 'w', newline='',encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(rows)
