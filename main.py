from football_web_scraper.utils.params import *
from football_web_scraper.football_web_scraper import get_data_dropdown, save_csv

url = URL
country_index = START_INDEX  # Start from START_INDEX

while True:
    # Get data
    print(f"Scraping data for country index {country_index}...")
    df = get_data_dropdown(url, country_index)

    # Check if the DataFrame is empty (indicating no such index)
    if df.empty:
        print(f"No element with index {country_index}, stopping.")
        break

    # Save data to CSV
    print(f"Saving data for country index {country_index}...")
    save_csv(df, country_index)

    # Increment the index for the next iteration
    country_index += 1

print('*********************************')
print("Data scraping and saving completed successfully")
print('*********************************')
