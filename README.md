This script allows you to scrape and extract random sentences from Wikipedia articles and save them in both DOCX and TXT files. To create a diverse and extensive set of files, multiple Wikipedia URL links are used because a single link may not provide enough sentences to generate 10,000 files, each containing 15 random sentences that start with letters.

Usage:
- The script starts by specifying a list of Wikipedia URLs (you can add more as needed) from which sentences will be extracted.

- It then extracts sentences from the Wikipedia articles and cleans the text by removing any numbers and brackets.

- After cleaning, the script identifies sentences ending with a period and separates them.

- For each URL, the script randomly selects sentences, ensuring that they start with letters, and creates sets of DOCX and TXT files.

- The number of DOCX and TXT files, as well as the number of sentences in each file, are defined in the script.

- The resulting files are saved in separate folders, with the DOCX files in the "docx_files" folder and TXT files in the "txt_files" folder.

- Finally, the script provides feedback about the number of sets of files created, with each set containing 15 random sentences. These files can be useful for various applications, such as testing and training data for natural language processing tasks.

Note: Multiple Wikipedia URLs are used to ensure a sufficient number of sentences for creating 10,000 files.
