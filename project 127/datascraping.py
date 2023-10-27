from bs4 import BeautifulSoup
import time
import pandas as pd

URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser = webdriver.Chrome()
browser.get(URL)


scraped_data = []


def scrape():

    for i in range():
        print()

    bright_star_table = soup.find("table", attrs={"class", "wikitable"})

    table_body = bright_star_table.find("tbody")

    table_rows = table_body.find_all("tr")

    for rows in table_rows:
        table_cols = rows.find_all("td")
        print(table_cols)

        temp_list = []
        for col_data in table_cols:

         print(cols_data.text)

            data = col_data.text.strip()

            temp_list.append(data)

            scraped_data.append(temp_list)
