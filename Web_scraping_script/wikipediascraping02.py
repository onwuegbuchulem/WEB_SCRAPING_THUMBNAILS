import re
import requests
import bs4
import os
import random
from docx import Document  # Import Document from docx

# List of Wikipedia URLs to scrape (add more as needed)
wikipedia_urls = [
    "https://en.wikipedia.org/wiki/Artificial_intelligence",
    "https://en.wikipedia.org/wiki/Machine_learning",
    "https://en.wikipedia.org/wiki/Data_science",
    "https://en.wikipedia.org/wiki/Computer_programming",
    # Add more URLs as needed
]

# Function to extract sentences from a Wikipedia page
def extract_sentences_from_wikipedia(url):
    page = requests.get(url)

    if page.status_code == 200:
        soup = bs4.BeautifulSoup(page.text, 'html.parser')
        texts = " ".join([element.text for element in soup.find_all('p')])
        return texts
    else:
        print(f"Failed to retrieve the Wikipedia page: {url}")
        return []

# Function to remove [] from the text
def remove_numbers_and_brackets(text):
    pattern = r'\[\d+\]'
    result = re.sub(pattern, '', text)
    return result

# Function to extract sentences ending with a period
def extract_sentences(text):
    sentence_pattern = r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s'
    sentences = re.split(sentence_pattern, text)
    return sentences

# Function to save sentences to .doc and .txt files
def save_to_docx_and_txt(sentences, num_files, sentences_per_file, docx_folder="docx_files", txt_folder="txt_files"):
    os.makedirs(docx_folder, exist_ok=True)
    os.makedirs(txt_folder, exist_ok=True)

    for i in range(num_files):
        selected_sentences = random.choices(sentences, k=sentences_per_file)

        selected_sentences = [sentence for sentence in selected_sentences if sentence and sentence[0].isalpha()]

        if len (selected_sentences) < sentences_per_file:
            additional_sentences = random.choices(sentences, k=sentences_per_file - len(selected_sentences))
            selected_sentences.extend(additional_sentences)

        selected_text = '\n'.join(selected_sentences)

        docx = Document()
        docx.add_paragraph(selected_text)
        docx_filename = os.path.join(docx_folder, f"{i + 1}.docx")
        docx.save(docx_filename)

        txt_filename = os.path.join(txt_folder, f"{i + 1}.txt")
        with open(txt_filename, "w", encoding="utf-8") as txt_file:
            txt_file.write(selected_text)

    print(f"{num_files} sets of .docx and .txt files, each containing {sentences_per_file} random sentences (beginning with letters), saved to separate folders.")

# Define the number of .doc and .txt files to create
num_files = 10000
sentences_per_file = 15

# Create folders for .doc and .txt files
docx_folder = "docx_files"
txt_folder = "txt_files"

# Call the function to save sentences to .doc and .txt files
for url in wikipedia_urls:
    result = remove_numbers_and_brackets(extract_sentences_from_wikipedia(url))
    sentences = extract_sentences(result)
    save_to_docx_and_txt(sentences, num_files, sentences_per_file, docx_folder, txt_folder)
