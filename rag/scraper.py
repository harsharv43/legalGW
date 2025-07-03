import requests
from bs4 import BeautifulSoup
import os
import re
from urllib.parse import urljoin

KEYWORDS = [
    "startup", "company", "corporate", "llp", "sebi", "investment", "shareholder", "partnership", "business", "enterprise", "fund", "angel", "venture", "incubator", "accelerator"
]

BASE_URL = "https://www.indiacode.nic.in"
ACTS_LIST_URL = "https://www.indiacode.nic.in/handle/123456789/1362/browse?type=act&sort_by=1&order=ASC&rpp=1000"


def fetch_law(url, save_dir="data/laws", meta=None):
    os.makedirs(save_dir, exist_ok=True)
    resp = requests.get(url)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.text, "html.parser")
        # Extract main content (placeholder logic)
        text = soup.get_text()
        law_id = url.split("/")[-1] or "law"
        with open(os.path.join(save_dir, f"{law_id}.txt"), "w", encoding="utf-8") as f:
            f.write(text)
        if meta:
            with open(os.path.join(save_dir, f"{law_id}.meta.txt"), "w", encoding="utf-8") as f:
                for k, v in meta.items():
                    f.write(f"{k}: {v}\n")
        print(f"Saved: {law_id}")
    else:
        print(f"Failed to fetch: {url}")

def crawl_and_fetch_acts():
    print("Crawling acts list...")
    resp = requests.get(ACTS_LIST_URL)
    if resp.status_code != 200:
        print("Failed to fetch acts list.")
        return
    soup = BeautifulSoup(resp.text, "html.parser")
    links = soup.find_all("a", href=True)
    for link in links:
        title = link.text.strip().lower()
        if any(kw in title for kw in KEYWORDS):
            act_url = urljoin(BASE_URL, link['href'])
            meta = {"title": link.text.strip(), "url": act_url}
            fetch_law(act_url, meta=meta)

def fetch_from_manual_list(file_path="manual_laws.txt"):
    if not os.path.exists(file_path):
        print(f"Manual list {file_path} not found.")
        return
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            url = line.strip()
            if url:
                fetch_law(url)

if __name__ == "__main__":
    # 1. Crawl and fetch relevant acts
    crawl_and_fetch_acts()
    # 2. Fetch from manual list
    fetch_from_manual_list() 