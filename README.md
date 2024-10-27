# python-data-scraper

## Overview
This repository contains a basic web data scraping program using Python, showcasing the use of two powerful libraries: **BeautifulSoup** and **Scrapy**. These tools allow for efficient extraction of data from websites.

## Libraries Used
- **BeautifulSoup**: A library for parsing HTML and XML documents. It makes it easy to navigate and search through the parse tree.
- **Scrapy**: A powerful framework for web scraping that allows you to extract data from websites and handle multiple requests efficiently.

## Limitations
- This code can only retrieve pages that do not require JavaScript to load the DOM and is designed for static HTML elements only. Further study and more complex programs are needed to handle dynamic content, making this repository serve as a basic foundation for data scraping.

## How to Run

### Running Scrapy
To run the Scrapy spider, use the following command in your terminal:

```bash
scrapy crawl matchaTokyo
scrapy crawl macanneTeam
```

Make sure you are in the correct directory where your Scrapy project is located and correct name of spider is entered.

### Running BeautifulSoup
To run the BeautifulSoup scraping script, use the following command in your terminal:

```bash
python .\data_scraper_BeautifulSoup.py
```

Ensure you have the necessary libraries installed by using the following commands:

```bash
pip install beautifulsoup4
pip install requests
pip install Scrapy
```

## Acknowledgements
- **BeautifulSoup**: [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- **Scrapy**: [Scrapy Installation Guide](https://doc.scrapy.org/en/latest/intro/install.html#intro-install)

## Author
Shania Francine T. Cloma

Feel free to contribute, raise issues, or ask questions!
