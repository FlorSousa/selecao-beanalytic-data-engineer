from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd
from google.oauth2 import service_account
def get_data_from_row(row):
    cells = row.find_elements(By.TAG_NAME,"td")
    return [cell.text for cell in cells]


def get_dataframe_from_scraping(url) -> pd.DataFrame: 
    with webdriver.Chrome() as driver:
        driver.get(url)
        select_element = driver.find_element(By.ID, "dt-length-0")
        select = Select(select_element)
        select.select_by_value('-1')
        table_element = driver.find_element(By.ID, "DataTables_Table_0")
        rows = table_element.find_elements(By.TAG_NAME, "tr")
        content = filter(lambda row_data: row_data !=[], list(map(get_data_from_row,rows)))
        filtered_content = [row[2:] for row in content]
        return pd.DataFrame.from_records(filtered_content,columns=["title","discount","price","rating","release_date","promo_end","promo_begin"])
    
if __name__ == "__main__":
    dataframe_games = get_dataframe_from_scraping(url="https://steamdb.info/sales/")
    dataframe_games["title"] = dataframe_games["title"].str.split("\n").str[0]
    dataframe_games["price"] = dataframe_games["price"].str.split("R\\$ ").str[1].str.replace(',','.').astype(float)
    dataframe_games["discount"] = dataframe_games["discount"].str.split("%").str[0]
    dataframe_games["rating"] = dataframe_games["rating"].str.split("%").str[0]
    print("Fim do scraping")
    import os
    from dotenv import load_dotenv
    load_dotenv()
    print("Conexão com bigQuery")
    key_path = os.getenv("PATH_TO_CLOUD_CREDENTIALS")
    credentials = service_account.Credentials.from_service_account_file(
        key_path, scopes=["https://www.googleapis.com/auth/cloud-platform"])
    dataframe_games.to_gbq(credentials=credentials,destination_table="beAnalytic.games",if_exists="replace")
    dataframe_games.to_csv("backup_games_data.csv",index=False)
    print("Extração completa")