# 🛒 Catalog Scraper Mini Project

A **modular, high-performance web scraper** designed for the
**University of Central Punjab (Faculty of IT & CS)**.\
This tool extracts product data from the **webscraper.io static
e-commerce test site**, navigating through hierarchical categories and
paginated listings.

------------------------------------------------------------------------

# 🚀 Overview

This scraper is built with a focus on **modularity, scalability, and
real-world crawling logic**.\
Instead of scraping a single page, the system:

-   Discovers **categories automatically**
-   Follows **subcategory links**
-   Handles **pagination**
-   Extracts **deep-level product specifications**
-   Produces a **clean dataset ready for analysis**

The goal is to simulate a **production-style catalog crawler** with
clean architecture.

------------------------------------------------------------------------

# 🛠️ Technical Stack

**Language** - Python 3.12+

**Package Manager** - uv (Extremely fast Python dependency resolver)

**Libraries** - BeautifulSoup4 → HTML parsing and DOM traversal -
Requests → HTTP networking - Pandas → Data cleaning, deduplication, and
CSV export

------------------------------------------------------------------------

# 📁 Project Structure

    catalog-scraper/
    ├── data/                # Output directory for CSV datasets
    ├── src/
    │   ├── main.py          # Orchestrator: Coordinates the scraping pipeline
    │   └── scraper/
    │       ├── crawler.py   # Discovery: Finds categories and subcategories
    │       ├── parsers.py   # Extraction: Scrapes details from product pages
    │       ├── exporters.py # IO: CSV generation and deduplication
    │       └── utils.py     # Helpers: URL resolution and string cleaning
    ├── pyproject.toml       # uv configuration and dependency manifest
    └── README.md            # Project documentation

------------------------------------------------------------------------

# ⚙️ Setup & Installation

## 1️⃣ Prerequisites

Make sure you have:

-   **Python 3.12 or higher**
-   **uv package manager**

Install uv if needed:

    pip install uv

------------------------------------------------------------------------

## 2️⃣ Install Dependencies

Initialize the virtual environment and install packages:

    python -m uv sync

------------------------------------------------------------------------

## 3️⃣ Run the Scraper

### Windows (PowerShell)

    $env:PYTHONPATH="."
    python -m uv run src/main.py

### macOS / Linux

    PYTHONPATH=. python -m uv run src/main.py

Running the script will:

1.  Discover categories
2.  Crawl paginated product lists
3.  Extract product information
4.  Clean and normalize the data
5.  Export the dataset to CSV

------------------------------------------------------------------------

# 🔄 Data Processing Logic

To ensure **high-quality data**, the scraper includes several
preprocessing steps.

### 1️⃣ Deduplication

Pandas removes duplicate records using the product URL as the primary
key.

    drop_duplicates(subset="product_url")

This prevents duplicate entries caused by overlapping categories.

------------------------------------------------------------------------

### 2️⃣ Price Normalization

Prices are cleaned by:

-   Removing currency symbols
-   Converting values to **float**

Example:

    "$799.00" → 799.00

This allows easier statistical analysis later.

------------------------------------------------------------------------

### 3️⃣ Whitespace Cleaning

All extracted text fields are normalized:

-   Remove leading/trailing spaces
-   Remove newline characters
-   Normalize spacing

------------------------------------------------------------------------

### 4️⃣ Resilient Scraping

The scraper is designed to **avoid crashes**:

-   try/except blocks
-   safe HTML element checks
-   fallback values when data is missing

This ensures the crawler continues running even if some pages contain
unexpected HTML structures.

------------------------------------------------------------------------

# 🌿 Git Branching Workflow

This project follows a **feature branching strategy**.

### Main Branches

**main** - Stable, production-ready code

**dev** - Integration branch for features

------------------------------------------------------------------------

### Feature Branches

**feature/catalog-navigation** - Category discovery logic

**feature/product-details** - Product page scraping logic

------------------------------------------------------------------------

### Fix Branches

**fix/url-resolution** - Fix relative URLs and pagination issues

**fix/deduplication** - Ensure unique product records

------------------------------------------------------------------------

# 📊 Output

After execution, the scraper generates:

    data/products.csv

The dataset includes fields such as:

-   product_name
-   price
-   description
-   rating
-   product_url
-   category

The CSV file is **analysis-ready** for tools like:

-   Pandas
-   Excel
-   Power BI
-   Tableau

------------------------------------------------------------------------

# ⚠️ Limitations

### JavaScript Websites

This scraper works only on **static HTML websites**.\
It does **not support JavaScript-heavy SPAs** (React, Angular, Vue).

For those, tools like:

-   Selenium
-   Playwright
-   Puppeteer

would be required.

------------------------------------------------------------------------

### Pagination Limit

Pagination stops automatically when:

-   The **Next button disappears**
-   No **new product URLs** are discovered

------------------------------------------------------------------------

# 🎯 Learning Objectives

This project demonstrates:

-   Real-world **web crawling architecture**
-   Modular **Python project structure**
-   Data cleaning using **Pandas**
-   Robust scraping with **BeautifulSoup**
-   Clean **Git branching workflow**

------------------------------------------------------------------------

# 👨‍💻 Author

**Mannal Aqil**\
Bachelor's in Data Science\
University of Central Punjab
