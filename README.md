# 💼 UCP Job Scraper Pipeline

A hybrid, production-style web scraping pipeline designed for the
University of Central Punjab (Faculty of IT & CS).

This tool extracts tech job listings from Canonical's Greenhouse job
board by combining the dynamic browser automation of Selenium with the
high-speed, structured extraction of Scrapy.

------------------------------------------------------------------------

## 🚀 Overview

This scraper is built to simulate a real-world data engineering pipeline
where data is passed between different systems.

Instead of relying on a single tool, the system:

-   Uses Selenium to render JavaScript, scroll dynamically, and bypass
    initial DOM restrictions.
-   Extracts target URLs into an intermediate dataset.
-   Passes the URLs to Scrapy for high-performance, concurrent crawling.
-   Extracts deep-level job specifications (skills, department,
    location).
-   Produces a clean dataset ready for Pandas analysis.

The goal is to demonstrate end-to-end integration, robust data
extraction, and strict version control.

------------------------------------------------------------------------

## 🛠️ Technical Stack

### Language

-   Python 3.12+

### Environment

-   Standard Python venv

### Libraries

-   Selenium → Browser automation, JavaScript rendering, and dynamic
    scrolling.
-   Scrapy → High-speed web crawling and structured data extraction.
-   Pandas → Data processing, text parsing, and analytical reporting.

------------------------------------------------------------------------

## 📁 Project Structure

    ucp_job_scraper/
    ├── analysis/
    │   └── analyze_jobs.py
    ├── data/
    │   ├── final/
    │   │   └── jobs.csv
    │   └── raw/
    │       └── job_links.csv
    ├── docs/
    │   └── report.md
    ├── scrapy_project/
    │   └── jobs_scraper/
    │       └── spiders/
    │           └── canonical.py
    ├── selenium_scripts/
    │   └── collect_links.py
    └── README.md

------------------------------------------------------------------------

## ⚙️ Setup & Installation

### 1️⃣ Prerequisites

-   Python 3.10 or higher
-   Google Chrome installed

### 2️⃣ Install Dependencies

``` bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install selenium scrapy pandas
```

------------------------------------------------------------------------

## ▶️ Run the Pipeline

### Phase 1: URL Extraction (Selenium)

``` bash
python selenium_scripts/collect_links.py
```

### Phase 2: Data Crawling (Scrapy)

``` bash
cd scrapy_project
scrapy crawl canonical -O ../data/final/jobs.csv
cd ..
```

### Phase 3: Trend Analysis (Pandas)

``` bash
python analysis/analyze_jobs.py
```

------------------------------------------------------------------------

## 🔄 Data Processing Logic

### Keyword Extraction (Regex)

``` python
re.findall(r'\b' + re.escape(skill) + r'\b', text_data)
```

### Fallback Data Parsing

-   Uses response.meta as fallback
-   Defaults missing locations to Remote/Unspecified
-   Cleans list items into readable format

### System Stability Flags

-   --no-sandbox
-   --disable-dev-shm-usage

------------------------------------------------------------------------

## 🌿 Git Branching Workflow

### Main Branches

-   main
-   develop

### Feature & Release Branches

-   feature/selenium-search
-   feature/scrapy-job-parser
-   feature/data-analysis
-   release/v1.0-assignment

------------------------------------------------------------------------

## 📊 Output

    data/final/jobs.csv

Includes:

-   Job title
-   Company name
-   Location
-   Department
-   Employment type
-   Job URL
-   Description
-   Skills

------------------------------------------------------------------------

## ⚠️ Limitations

### Dynamic DOM Changes

HTML structure may change; selectors may need updates.

### Execution Speed

Selenium is slower but required for JavaScript rendering.

------------------------------------------------------------------------

## 🎯 Learning Objectives

-   Multi-tool pipeline integration
-   Handling dynamic web content
-   Scalable crawling with Scrapy
-   Data cleaning with Pandas
-   Git workflow discipline

------------------------------------------------------------------------

## 👨‍💻 Author

Mannal Aqil\
Bachelor's in Data Science\
University of Central Punjab
