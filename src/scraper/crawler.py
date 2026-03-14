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
    links = soup.find_all('a', class_='category-link')
    for link in links:
        name_tag = link.find('span', itemprop='name')
        name = name_tag.text.strip() if name_tag else link.text.strip()
        url = resolve_url(BASE_URL, link.get('href'))
        categories.append({'name': name, 'url': url})
    return categories

def discover_subcategories(category_url):
    """Finds subcategories (like Laptops, Tablets) on a category page."""
    soup = get_soup(category_url)
    subcategories = []
    if not soup: return subcategories
    # Subcategories are in the sidebar under the active category
    links = soup.select('ul#side-menu li.nav-item ul.nav.flex-column li a')
    for link in links:
        url = resolve_url(BASE_URL, link.get('href'))
        subcategories.append({
            'name': link.text.strip(),
            'url': url
        })
    return subcategories

def get_product_links(page_url):
    soup = get_soup(page_url)
    links = []
    if not soup: return links
    product_anchors = soup.find_all('a', class_='title')
    for a in product_anchors:
        link = resolve_url(BASE_URL, a.get('href'))
        if link: links.append(link)
    return links