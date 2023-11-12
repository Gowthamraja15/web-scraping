# web-scraping

# AniWatch Anime Genre Scraper

## Overview

This Python script scrapes anime genres from the AniWatch website and stores the results in an Excel file. It utilizes BeautifulSoup for web scraping and requests to fetch the HTML content.

## Prerequisites

Make sure you have the required Python libraries installed:

- BeautifulSoup 4: `pip install beautifulsoup4`
- Requests: `pip install requests`
- Openpyxl: `pip install openpyxl`

## Usage

1. Clone the repository or download the script.
2. Run the script using Python: `python script_name.py` (replace `script_name.py` with the actual name of your script).

## Description

- The script sends a GET request to AniWatch's search page for the keyword "top animies."
- It parses the HTML content using BeautifulSoup to extract anime genres.
- The genres are saved to an Excel file named "aniwatch-genre.xlsx" with a single column header "genres."

## File Structure

- `aniwatch-genre.xlsx`: Excel file containing the scraped anime genres.

## Contributing

Feel free to contribute by opening issues or submitting pull requests.

## License

This project is licensed under the [MIT License](LICENSE).

---

Adjust the content as needed, and consider adding more sections such as "Installation," "Troubleshooting," or "Acknowledgments" depending on the complexity of your project.
