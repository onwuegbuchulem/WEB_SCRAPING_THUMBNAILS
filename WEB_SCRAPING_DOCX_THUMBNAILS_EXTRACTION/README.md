Wikipedia Web Scraping, Thumbnail Extraction, and Matching Process Project

Project Description
This comprehensive project involves web scraping text files from Wikipedia, saving random texts of 15 sentences in 10,000 docx files, and then extracting thumbnails from the thumbcache.dbs of these docx files. The extracted thumbnails are based on the resolutions of 48 for medium size thumbnails (from thumbcache_48.db), 96 for large size thumbnails (from thumbcache_96.db), and 256 for extra-large thumbnails (from thumbcache_256.db), using a VBA script. To accommodate GitHub's limitation of 1,000 files per folder, the extracted thumbnails are organized into 10 folders for each thumbcache.db resolution.

Features
Web scrape text files from Wikipedia.
Generate 10,000 docx files with random texts.
Extract thumbnails from docx files with 48, 96, and 256 resolutions.
Organize and save the thumbnails in separate folders for each resolution.
Easy customization and extensibility.
Getting Started
Prerequisites:

Python for web scraping.
Microsoft Word for processing docx files.
VBA scripting for thumbnail extraction.
Installation:

Clone this repository to your local machine.
bash
Copy code
git clone https://github.com/yourusername/your-repo.git
Set up the Python environment for web scraping.
bash
Copy code
pip install -r requirements.txt
Prepare your environment for VBA script execution.
Usage
Web Scraping:

Run the Python web scraping script to fetch Wikipedia text files.
Generating Docx Files:

Run the script to create 10,000 docx files with random text.
Thumbnail Extraction:

Execute the VBA script to extract thumbnails from docx files (from thumbcache_48.db, thumbcache_96.db, and thumbcache_256.db).
Organizing Thumbnails:

After extraction, the script will automatically organize and save the thumbnails into folders according to their resolutions.
Thumbnail Matching Process:

Follow the provided steps to accurately match the extracted thumbnails to their corresponding parent files.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Wikipedia for providing valuable data.
The open-source community for Python and VBA.