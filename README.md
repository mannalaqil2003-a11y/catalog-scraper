# 💼 UCP Job Scraper Pipeline

A **hybrid, production-style web scraping pipeline** designed for the **University of Central Punjab (Faculty of IT & CS)**.  
This tool extracts tech job listings from **Canonical's Greenhouse job board** by combining the dynamic browser automation of Selenium with the high-speed, structured extraction of Scrapy.

---

# 🚀 Overview

This scraper is built to simulate a **real-world data engineering pipeline** where data is passed between different systems.  
Instead of relying on a single tool, the system:

-   Uses **Selenium** to render JavaScript, scroll dynamically, and bypass initial DOM restrictions.
-   Extracts target URLs into an intermediate dataset.
-   Passes the URLs to **Scrapy** for high-performance, concurrent crawling.
-   Extracts **deep-level job specifications** (skills, department, location).
-   Produces a **clean dataset ready for Pandas analysis**.

The goal is to demonstrate end-to-end integration, robust data extraction, and strict version control.

---

# 🛠️ Technical Stack

**Language** - Python 3.12+

**Environment** - Standard Python virtual environment (`venv`)

**Libraries** 
-   **Selenium** → Browser automation, JavaScript rendering, and dynamic scrolling
-   **Scrapy** → High-speed web crawling and structured data extraction
-   **Pandas** → Data processing, text parsing, and analytical reporting

---

# 📁 Project Structure

    ucp_job_scraper/
    ├── analysis/            # Analytical scripts for hiring trends
    │   └── analyze_jobs.py  # Pandas logic for skill/location extraction
    ├── data/                # Output directory (ignored by Git)
    │   ├── final/           # jobs.csv (Scrapy output)
    │   └── raw/             # job_links.csv (Selenium output)
    ├── docs/                # Project documentation and findings
    │   └── report.md        # Summary of hiring trends
    ├── scrapy_project/      # Scrapy framework files and spiders
    │   └── jobs_scraper/
    │       └── spiders/
    │           └── canonical.py  # Spider logic for job detail pages
    ├── selenium_scripts/    # Browser automation scripts
    │   └── collect_links.py # Link extraction and filtering logic
    └── README.md            # Project documentation

---

# ⚙️ Setup & Installation

## 1️⃣ Prerequisites

Make sure you have:
-   **Python 3.10 or higher**
-   **Google Chrome** installed on your machine

---

## 2️⃣ Install Dependencies

Initialize the virtual environment and install the required packages:

### Windows (PowerShell)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install selenium scrapy pandas
macOS / Linux
Bash
python -m venv .venv
source .venv/bin/activate
pip install selenium scrapy pandas
3️⃣ Run the Pipeline
The pipeline must be run in three distinct phases:

Phase 1: URL Extraction (Selenium)
Bash
python selenium_scripts/collect_links.py
Navigates the job board, scrolls to load elements, and saves links to data/raw/job_links.csv.

Phase 2: Data Crawling (Scrapy)
Bash
cd scrapy_project
scrapy crawl canonical -O ../data/final/jobs.csv
cd ..
Consumes the raw CSV, visits every job page, extracts structured data, and saves to data/final/jobs.csv.

Phase 3: Trend Analysis (Pandas)
Bash
python analysis/analyze_jobs.py
Reads the final CSV and prints a business intelligence report to the terminal.

🔄 Data Processing Logic
To ensure high-quality insights, the analysis script includes several preprocessing steps.

1️⃣ Keyword Extraction (Regex)
Skills are extracted from the raw job description text by matching whole words using Regular Expressions. This prevents false positives (e.g., matching "go" inside the word "algorithm").

2️⃣ Fallback Data Parsing
The Scrapy spider is designed to avoid missing data:

Uses response.meta to fallback to Selenium's job title if the Greenhouse DOM changes.

Defaults missing locations to Remote/Unspecified.

Cleans and joins list items (<li>) into comma-separated skill strings.

3️⃣ System Stability Flags
Selenium is configured with low-level Chrome flags (--no-sandbox, --disable-dev-shm-usage) to prevent memory crashes during automated scrolling.

🌿 Git Branching Workflow
This project follows a strict professional feature branching strategy.

Main Branches
main - Stable, production-ready release code.

develop - Integration branch where all features were merged first.

Feature & Release Branches
feature/selenium-search - Browser automation and link collection.

feature/scrapy-job-parser - Spider framework and data extraction.

feature/data-analysis - Pandas reporting logic.

release/v1.0-assignment - Final documentation and project hardening.

📊 Output
After execution, the pipeline generates:
data/final/jobs.csv

The dataset includes required assignment fields:

Job title

Company name

Location

Department / team

Employment type

Job URL

Job description

Required skills

The final output is passed into a Pandas report that calculates top skills, top locations, and entry-level role availability, which is ready for tools like Excel, Power BI, or Tableau.

⚠️ Limitations
Dynamic DOM Changes
Job boards (like Greenhouse and Lever) frequently change their HTML class names (e.g., swapping <div class="opening"> for <tr class="job-post">). If the scraper fails to find elements, the CSS selectors in collect_links.py and canonical.py must be updated to match the live site.

Execution Speed
Because Phase 1 uses a real Chrome browser instance to handle JavaScript, it is intentionally slower than pure HTML parsing to avoid triggering anti-bot protections.

🎯 Learning Objectives
This project demonstrates:

Integration of multiple distinct technologies into a single data pipeline

Handling dynamic, JavaScript-rendered content via Browser Automation

Scalable, concurrent web crawling via Scrapy

Data cleaning and aggregation using Pandas

Strict Git workflow discipline (Branching, Merging, Tagging)

👨‍💻 Author
Mannal Aqil

Bachelor's in Data Science

University of Central Punjab
