## Web Scraper in Python

This Python script allows users to scrape websites by entering a URL and selecting whether to extract all links or the HTML code of the page. The result is saved in a `.txt` file.

## Features

- **Input URL**: Enter the URL of the website to scrape.
- **Choose what to scrape**: Either scrape all links (`<a>` tags) or the full HTML of the page.
- **Save results**: Results are saved to `parsed_links.txt` (for links) or `parsed_html.txt` (for HTML code).

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library

## Installation

1. Clone the repository or download the script.
2. Install the required libraries by running:

 ```bash

   pip install requests beautifulsoup4
