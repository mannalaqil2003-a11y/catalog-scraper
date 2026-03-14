from urllib.parse import urljoin

def resolve_url(base_url, relative_path):
    """Joins a base URL with a relative path safely."""
    if not relative_path:
        return None
    return urljoin(base_url, relative_path)

def clean_price(price_str):
    """Converts '$123.45' into float 123.45."""
    if not price_str:
        return 0.0
    # Remove currency symbols and commas, then convert to float
    clean_str = price_str.replace('$', '').replace(',', '').strip()
    try:
        return float(clean_str)
    except ValueError:
        return 0.0

def clean_text(text):
    """Removes extra whitespace and handles empty fields."""
    if not text:
        return ""
    return " ".join(text.split())