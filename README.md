
PART I: Wikipedia Web Scraping

Project Description
This project encompasses the extraction of text files from Wikipedia through web scraping. It involves saving random texts of 15 sentences into 10,000 docx files and subsequently extracting thumbnails from the thumbcache.dbs associated with these files. Thumbnails are extracted in three resolutions: 48 for medium-size (from thumbcache_48.db), 96 for large size (from thumbcache_96.db), and 256 for extra-large (from thumbcache_256.db). The extraction process utilizes a VBA script. To accommodate GitHub's restriction of 1,000 files per folder, the extracted thumbnails are organized into 10 folders for each thumbcache.db resolution.

Features
Web scraping of text files from Wikipedia.
Generation of 10,000 docx files containing random text.
Extraction of thumbnails from docx files in resolutions of 48, 96, and 256.
Automatic organization and storage of thumbnails in separate folders for each resolution.
Easy customization and extensibility.
Getting Started
Prerequisites:

Python for web scraping.
Microsoft Word for processing docx files.
VBA scripting for thumbnail extraction.
Installation:

Clone this repository to your local machine.

git clone https://github.com/yourusername/your-repo.git
Set up the Python environment for web scraping.

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

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Wikipedia for providing valuable data.
The open-source community for Python and VBA.


PART II: Thumbnail Extraction and Matching Process

Overview
This readme provides a step-by-step guide for the extraction and matching of thumbnails to their corresponding parent files. Ensure that no other folders are open during this process.

Steps

Set Folder View to Details:
Navigate to the folder containing the target file.
Set the view to "Details" for optimal visibility.

Clear Thumbcache.db Files:
Open File Explorer and navigate to:
C:\Users\{user_name}\AppData\Local\Microsoft\Windows\Explorer
Delete all thumbcache.db files in this directory.

Change Folder View Settings:
In the folder containing the file, click on the "View" tab.
Change the view settings as required.

Scroll Down Row by Row:
Gently scroll down row by row in the folder window to ensure all files are brought into view.

Refresh Thumbcache.db:
Refresh the thumbcache.db folder window to update the cache.

Extract Thumbnails:
Use Thumbcache Viewer to extract thumbnails from the refreshed cache.

Export Thumbnails to CSV:
Export the extracted thumbnails to a CSV file.

Match Thumbnails to Parent Files:
Utilize a Python script to match the thumbnails to their corresponding parent files.

Important Note
Ensure the accuracy of the matching process by carefully following each step. This guide assumes the use of Thumbcache Viewer and a Python script for matching. Adjustments may be needed based on specific tools or scripts employed.

Happy thumbnail extraction and matching!