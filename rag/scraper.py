import requests
from bs4 import BeautifulSoup
import os

def fetch_law(url, save_dir="data/laws"):
    os.makedirs(save_dir, exist_ok=True)
    resp = requests.get(url)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.text, "html.parser")
        # Extract main content (placeholder logic)
        text = soup.get_text()
        law_id = url.split("/")[-1] or "law"
        with open(os.path.join(save_dir, f"{law_id}.txt"), "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Saved: {law_id}")
    else:
        print(f"Failed to fetch: {url}")

if __name__ == "__main__":
    # Example: fetch a law page (replace with actual URLs or loop over many)
    fetch_law("https://www.indiacode.nic.in/show-data?actid=AC_CEN_5_23_00001_195615_1517807320565&type=act&year=1956&actno=1") 