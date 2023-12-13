# Football Data Scraping Project
## Overview
This project is designed to scrape football match data from [Adam Choi's Detailed Football Statistics](https://www.adamchoi.co.uk/overs/detailed). The script extracts information about football matches, including dates, home teams, scores, and away teams, and saves this data into a CSV file for further analysis.

## Features
- Scrapes match data including dates, home teams, scores, and away teams.
- Data is sourced from the 'All matches' section of the website.
- Capability to select data based on specific countries via a dropdown menu.
- Extracted data is saved in a structured CSV format.

## Prerequisites
Before running the project, ensure you have the following installed:

- Python (3.x)
- Selenium WebDriver
- ChromeDriver (compatible with your Chrome version)

## Installation
1. Clone the repository:
```
git clone https://github.com/Mldng/Football_Scrapping
```
2. Navigate to the cloned directory:
```
cd Football_Scrapping
```
3. Install required Python packages:
```
pip install -r requirements.txt
```

## Usage
To run the scraping script, execute the following command in the terminal:
```
python main.py
```

## Configuration
- The script uses Chrome WebDriver; ensure it is installed and its path is correctly set up.
- Modify the utils.params module as per your configuration needs (if applicable).

## Output
The scraped data is saved in the csv directory, named according to the country index (e.g., football_data_0.csv).

## Disclaimer
This project is intended for educational purposes only. Be aware of the terms of service of the website and ensure that your usage complies with their rules regarding web scraping.

## Contributing
Contributions to the project are welcome. Please ensure you follow the contribution guidelines provided.
