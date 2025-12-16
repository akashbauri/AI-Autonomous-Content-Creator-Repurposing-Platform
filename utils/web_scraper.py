import requests
from bs4 import BeautifulSoup

def extract_website_content(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = [p.get_text() for p in soup.find_all("p")]
        return " ".join(paragraphs[:30])
    except Exception as e:
        return f"Error reading website: {e}"
