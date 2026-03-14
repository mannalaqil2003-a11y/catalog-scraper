import pandas as pd
import os

def export_to_csv(data, filename):
    """Saves the product list to a CSV file."""
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    df = pd.DataFrame(data)
    # Deduplication requirement
    df = df.drop_duplicates(subset=['product_url'])
    df.to_csv(filename, index=False)
    print(f"Saved {len(df)} products to {filename}")
    return df

def export_summary(df, filename):
    """Generates the category_summary.csv report."""
    summary = df.groupby(['category', 'subcategory']).agg(
        total_products=('product_title', 'count'),
        average_price=('price', 'mean'),
        min_price=('price', 'min'),
        max_price=('price', 'max')
    ).reset_index()
    
    # Requirement: Count missing descriptions
    summary['missing_descriptions'] = df[df['description'] == ""].groupby(['category', 'subcategory'])['description'].count().reset_index(drop=True)
    summary.fillna(0, inplace=True)
    
    summary.to_csv(filename, index=False)
    print(f"Summary report saved to {filename}")