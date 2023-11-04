import os
from wand.image import Image

# Directory containing your PDF files
pdf_folder = "/home/ubuntu/Web Scraping/pdf"

# Directory where you want to save the JPEG thumbnails
thumbnail_folder = "/home/ubuntu/Web Scraping/thumbnails"

# Ensure the output directory exists
os.makedirs(thumbnail_folder, exist_ok=True)

# Loop through each PDF file in the input directory
for pdf_file in os.listdir(pdf_folder):
    if pdf_file.endswith(".pdf"):
        pdf_path = os.path.join(pdf_folder, pdf_file)

        # Open the PDF file
        with Image(filename=pdf_path) as img:
            # Generate the thumbnail filename
            thumbnail_filename = os.path.splitext(pdf_file)[0] + ".jpg"
            thumbnail_path = os.path.join(thumbnail_folder, thumbnail_filename)

            # Save the PDF page as a JPEG thumbnail
            img.save(filename=thumbnail_path)

            print(f"Converted {pdf_file} to {thumbnail_filename}")
