from selenium import webdriver
from msedge.selenium_tools import EdgeOptions
import time
from datetime import datetime
import winsound


def ShowTime():
    now = datetime.now()
    current_time = now.strftime('%H:%M:%S')
    return current_time


def GetPrices(item_ID, price_limit):
    options = EdgeOptions()
    options.use_chromium = True
    options.add_argument("headless")
    options.add_argument("disable-gpu")

    driver = webdriver.Chrome('C:/Users/kevin/Documents/PyCharmProjects/TCC-Scraper/msedgedriver.exe',
                              options=options)
    driver.get(
        f'https://us.tamrieltradecentre.com/pc/Trade/SearchResult?ItemID={item_ID}&SortBy=Price&Order=asc&page=1')


    item_name = driver.find_element_by_xpath('//*[@id="search-result-view"]/div[1]/div/table/tbody/tr[1]/td[1]/div[1]')

    duration = 1000
    freq = 440

    dict_price = {}
    dict_time = {}
    dict_location = {}
    dict_guildname = {}

    for i in range(1, 20, 2):
        dict_price[i] = f'//*[@id="search-result-view"]/div[1]/div/table/tbody/tr[{i}]/td[4]/span[1]'
        dict_time[i] = f'//*[@id="search-result-view"]/div[1]/div/table/tbody/tr[{i}]/td[5]'
        dict_location[i] = f'//*[@id="search-result-view"]/div[1]/div/table/tbody/tr[{i}]/td[3]/div[1]'
        dict_guildname[i] = f'//*[@id="search-result-view"]/div[1]/div/table/tbody/tr[{i}]/td[3]/div[2]'

    for i in range(1, 20, 2):
        price = driver.find_element_by_xpath(dict_price[i])
        price_str = (price.text.replace(',', ''))
        price_float = float(price_str)
        price_int = int(price_float)
        age = driver.find_element_by_xpath(dict_time[i])
        location = driver.find_element_by_xpath(dict_location[i])
        guildname = driver.find_element_by_xpath(dict_guildname[i])

        if '5 Hour ago' == age.text or '2 Minute ago' == age.text or '3 Minute ago' == age.text:
            if price_int < price_limit:
                print(f'{item_name.text}: {price.text} , Posted: {age.text}')
                print(f'Location: {location.text}, Guild Name: {guildname.text}')
                # winsound.Beep(freq,duration)


    print(f'Price Checked for: {item_name.text},', 'at', ShowTime(), 'PM', '- Waiting 10 Seconds')
    time.sleep(10)


while True:
    try:
        GetPrices(11807, 300000)  # Aetherial Dust
        GetPrices(211, 100000)  # Dreugh Wax
        GetPrices(6132, 100000)  # Perfect Roe
        GetPrices(5687, 100000)  # Tempering Alloy
        GetPrices(17927, 100000)  # Chromium Grains

    except:
        print('We got an error on our hands BOIIISSS')
        pass

