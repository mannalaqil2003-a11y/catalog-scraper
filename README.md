Catalog Scraper Mini Project
Project Overview

This project is a modular web scraper developed for the University of Central Punjab (Faculty of IT & CS).

It is designed to scrape the webscraper.io static e-commerce test site. The system navigates categories and subcategories, handles pagination, extracts detailed product information from individual detail pages, and exports cleaned data into CSV formats.

Technical Stack

Language: Python 3.12+
Package Manager: uv (Fast Python package installer and resolver)

Libraries

BeautifulSoup4 – HTML parsing and data extraction

Requests – Handling HTTP network calls

Pandas – Data manipulation, deduplication, and summary reporting

Project Structure
catalog-scraper/
├── data/                   # Generated CSV datasets
├── src/
│   ├── main.py             # Entry point / Coordinator
│   └── scraper/
│       ├── crawler.py      # Navigation & Discovery logic
│       ├── parsers.py      # Extraction & HTML parsing
│       ├── exporters.py    # CSV generation & Deduplication
│       └── utils.py        # URL resolution & Data cleaning
├── pyproject.toml          # uv configuration and dependencies
└── README.md               # Project documentation
Setup & Installation
1. Prerequisites

Ensure you have Python installed. This project uses uv for dependency management.

2. Install Dependencies

Initialize the environment and install required packages using uv:

python -m uv sync
3. Running the Scraper

Run the full scraping pipeline and generate the output files:

$env:PYTHONPATH = "."; python -m uv run src/main.py
Git Branching Workflow

This project follows a strict branching strategy:

main – Stable, production-ready code

dev – Main integration branch

feature/catalog-navigation – Discovery of categories/subcategories

feature/product-details – Extraction of product detail pages

fix/url-resolution – Handling relative paths for images and pagination

fix/deduplication – Ensuring unique records in the final dataset

Data Processing Logic
Deduplication

Uses Pandas drop_duplicates() on the product_url field to ensure no duplicate data.

Cleaning

Prices are stripped of currency symbols

Converted to float values

Whitespace normalized across text fields

Error Handling

try-except blocks for network requests

Safe checks for missing HTML elements

Prevents scraper crashes

Assumptions & Limitations

The scraper assumes the static version of the test site (no JavaScript rendering required).

Pagination traversal stops once no new product links are discovered.
