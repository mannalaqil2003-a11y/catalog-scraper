from src.scraper.utils import clean_price, clean_text, resolve_url

def parse_product_details(html_content, url, category, subcategory, page_num):
    """Extracts all required fields from a product detail page."""
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extract data using the specific classes/tags from the site
    title = soup.find('h4', class_=None).text if soup.find('h4', class_=None) else ""
    if not title: # Fallback for some page structures
        title = soup.select_one('div.caption h4:nth-of-type(2)').text if soup.select_one('div.caption h4:nth-of-type(2)') else "N/A"

    price_raw = soup.find('h4', class_='price').text if soup.find('h4', class_='price') else "0"
    description = soup.find('p', class_='description').text if soup.find('p', class_='description') else ""
    reviews = soup.find('p', class_='review-count').text if soup.find('p', class_='review-count') else "0"
    
    # For image URL
    img_tag = soup.find('img', class_='image')
    img_url = resolve_url(url, img_tag.get('src')) if img_tag else ""

    return {
        'category': category,
        'subcategory': subcategory,
        'product_title': clean_text(title),
        'price': clean_price(price_raw),
        'product_url': url,
        'image_url': img_url,
        'description': clean_text(description),
        'review_count': clean_text(reviews),
        'page_number': page_num
    }