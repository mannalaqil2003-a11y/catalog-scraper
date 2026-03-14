import requests
from src.scraper.crawler import discover_categories, discover_subcategories, get_product_links, get_soup
from src.scraper.parsers import parse_product_details
from src.scraper.exporters import export_to_csv, export_summary

def main():
    all_products = []
    print("🚀 Starting Scraper...")

    categories = discover_categories()
    
    for cat in categories:
        print(f"📂 Processing Category: {cat['name']}")
        subcategories = discover_subcategories(cat['url'])
        
        # If no subcategories, process the category itself as a listing
        if not subcategories:
            subcategories = [{'name': 'General', 'url': cat['url']}]

        for sub in subcategories:
            print(f"  └─ Subcategory: {sub['name']}")
            
            # Simple Pagination Loop
            page = 1
            while True:
                page_url = f"{sub['url']}?page={page}"
                print(f"    📄 Scraping Page {page}...")
                
                product_links = get_product_links(page_url)
                if not product_links:
                    break # No more products/pages
                
                for link in product_links:
                    # Visit Product Detail Page
                    response = requests.get(link)
                    if response.status_code == 200:
                        product_data = parse_product_details(
                            response.text, link, cat['name'], sub['name'], page
                        )
                        all_products.append(product_data)
                
                page += 1
                if page > 5: break # Safety limit for testing

    # Export Data
    if all_products:
        df = export_to_csv(all_products, "data/products.csv")
        export_summary(df, "data/category_summary.csv")
    else:
        print("❌ No data collected.")

if __name__ == "__main__":
    main()