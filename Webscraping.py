from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import datetime
import pandas as pd

PATH ="C:\Program Files (x86)\chromedriver.exe"
cService=webdriver.ChromeService(executable_path=PATH)
driver = webdriver.Chrome(service = cService)
driver.get("https://in.tradingview.com/markets/stocks-india/market-movers-all-stocks/")


performance_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "performance"))
)
performance_button.click()


# Click on the Load More button until all rows are loaded
while True:
    try:
        loadmore=driver.find_element(By.XPATH, "//button[contains(@class, 'button-SFwfC2e0 button-D4RPB3ZC size-xlarge-D4RPB3ZC color-gray-D4RPB3ZC variant-secondary-D4RPB3ZC apply-overflow-tooltip apply-overflow-tooltip--check-children-recursively apply-overflow-tooltip--allow-text')]")
        loadmore.click()
    except:
        break

table_data = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//table[@class='table-Ngq2xrcG']"))
)

# Extract the text from the table
table_html = table_data.get_attribute('outerHTML')
wdf = pd.read_html(table_html)[0]
now = str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
wdf.to_csv('stocks'+now+'.csv', index=False)
print(wdf.head())
# Close the browser
driver.quit()