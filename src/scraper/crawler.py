import requests
from bs4 import BeautifulSoup
from src.scraper.utils import resolve_url

BASE_URL = "https://webscraper.io/test-sites/e-commerce/static"

def get_soup(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return BeautifulSoup(response.text, 'html.parser')
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def discover_categories():
    soup = get_soup(BASE_URL)
    categories = []
    if not soup: return categories

    # Based on your HTML: <a href="..." class="category-link nav-link">
    links = soup.find_all('a', class_='category-link')
    for link in links:
        name = link.find('span', itemprop='name').text.strip()
        url = resolve_url(BASE_URL, link.get('href'))
        categories.append({'name': name, 'url': url})
    return categories

def get_product_links(page_url):
    """Finds all individual product detail links on a listing page."""
    soup = get_soup(page_url)
    links = []
    if not soup: return links

    # Product links are in <h4> <a class="title">
    product_anchors = soup.find_all('a', class_='title')
    for a in product_anchors:
        link = resolve_url(BASE_URL, a.get('href'))
        if link:
            links.append(link)
    return links