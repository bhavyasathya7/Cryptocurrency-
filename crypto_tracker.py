from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

options = webdriver.ChromeOptions()
options.add_argument("--headless")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

driver.get("https://coinmarketcap.com/")
time.sleep(5)

crypto_data = []

rows = driver.find_elements(By.XPATH, "//tbody/tr")[:10]

for row in rows:
    try:
        name = row.find_element(
            By.XPATH,
            ".//p[contains(@class,'coin-item-name')]"
        ).text

        price = row.find_element(By.XPATH, ".//td[4]").text
        change_24h = row.find_element(By.XPATH, ".//td[5]").text
        market_cap = row.find_element(By.XPATH, ".//td[8]").text

        crypto_data.append({
            "Coin Name": name,
            "Price": price,
            "24h Change": change_24h,
            "Market Cap": market_cap
        })

    except:
        pass

df = pd.DataFrame(crypto_data)

print(df)

df.to_csv("crypto_prices.csv", index=False)

driver.quit()