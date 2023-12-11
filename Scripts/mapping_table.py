import csv
import os

# Input CSV file
csv_file_path = 'Thumbnail256csv/Thumbnail256.csv'  # You can also generate tables for Thumbnail96csv/Thumbnail96.csv and
output_folder = 'mappingTableJPG'                   # Thumbnail48csv/Thumbnail48.csv

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Create a mapping between values and row numbers
mapping = {}
with open(csv_file_path, 'r', newline='', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file)

    # Read the header row
    header = next(reader)

    for row_number, row in enumerate(reader, start=1):
        # Assuming the first column is Thumbnail Filename and the second is Parent Filename
        thumbnail_filename = row[0]
        parent_filename = f"{row_number}.docx"
        mapping[thumbnail_filename] = parent_filename

# Save the resulting mapping to a text file with the specified header
output_file_path = os.path.join(output_folder, 'mapping.txt')
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    # Write the specified header
    output_file.write("Thumbnails Filenames: Parent Filenames\n")
    
    # Write the mapping
    for thumbnail_filename, parent_filename in mapping.items():
        output_file.write(f"{thumbnail_filename} : {parent_filename}\n")

print(f"Mapping saved to: {output_file_path}")
