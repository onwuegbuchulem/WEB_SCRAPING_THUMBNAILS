import re
import requests
import bs4
import os
import random
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

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

# Function to save sentences to PDF files
def save_to_pdf(sentences, num_files, sentences_per_file, pdf_folder="pdf_files"):
    os.makedirs(pdf_folder, exist_ok=True)
    
    styles = getSampleStyleSheet()
    pdfs = []
    
    for i in range(num_files):
        selected_sentences = random.choices(sentences, k=sentences_per_file)
        selected_text = ' '.join(selected_sentences)

        pdf_filename = os.path.join(pdf_folder, f"{i + 1}.pdf")
        
        doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
        story = []
        paragraph = Paragraph(selected_text, styles['Normal'])
        story.append(paragraph)
        doc.build(story)
        
        print(f"Saved {pdf_filename}")

# Define the number of PDF files and sentences per file
num_files = 10000
sentences_per_file = 25

# Create a folder for PDF files
pdf_folder = "pdf_files"

# Loop through Wikipedia URLs and process each page
for url in wikipedia_urls:
    result = remove_numbers_and_brackets(extract_sentences_from_wikipedia(url))
    sentences = extract_sentences(result)
    save_to_pdf(sentences, num_files, sentences_per_file, pdf_folder)
