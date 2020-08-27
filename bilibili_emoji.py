import requests
from selenium import webdriver
import time
import os
import json

#init webdriver with Chrome
driver = webdriver.Chrome()
url = "https://passport.bilibili.com/login"

driver.get(url)
if os.path.exists('bilibili.cookie'):
    #automatically login
    with open('bilibili.cookie', 'r') as f:
        js = f.read()
        cookies = json.loads(js)
        f.close()
    for i in cookies:
        print(i)
        driver.add_cookie(i)
    driver.get(url)
    input("it should be logged in. if there's something wrong, please manually fix it.")
else:    
    #manually login
    input("press any key to continue after you logged in.")
    cookies = driver.get_cookies()
    js = json.dumps(cookies)
    with open('bilibili.cookie', 'w') as f:
        f.write(js)
        f.close()


#access bilibili timeline
time.sleep(1)
url = "https://t.bilibili.com/?spm_id_from=333.851.b_696e7465726e6174696f6e616c486561646572.28"
driver.get(url)
time.sleep(2)

#find emoji button
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/div[1]/button').click()
time.sleep(2)

#fetch bilibili_emoji
try:
    for i in range(1, 100):
        emoji = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/div[1]/div/div/div[3]/div[1]/ul/li[{0}]/div'.format(i))

        emoji_title = emoji.get_attribute('title')
        emoji_title = emoji_title[1:-1]
        emoji_style = emoji.get_attribute('style')
        emoji_link = 'https:' + emoji_style.split('"')[1]

        print(emoji_title)
        print(emoji_link)
        print()
        content = requests.get(emoji_link).content
        with open('bilibili_emoji/emoji/{0}.png'.format(emoji_title), 'wb') as f:
            f.write(content)
            f.close()
except Exception as e:
    print(e)

#find hot_word button and fetch
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/div[1]/div/div/div[3]/div[2]/ul/li[2]/div').click()
time.sleep(2)
try:
    for i in range(1, 100):
        emoji = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/div[1]/div/div/div[3]/div[1]/ul/li[{0}]/div'.format(i))

        emoji_title = emoji.get_attribute('title')
        emoji_title = emoji_title[1:-1]
        emoji_style = emoji.get_attribute('style')
        emoji_link = 'https:' + emoji_style.split('"')[1]

        print(emoji_title)
        print(emoji_link)
        print()
        content = requests.get(emoji_link).content
        with open('bilibili_emoji/hot/{0}.png'.format(emoji_title), 'wb') as f:
            f.write(content)
            f.close()
except Exception as e:
    print(e)

#find tv button and fetch
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/div[1]/div/div/div[3]/div[2]/ul/li[3]/div').click()
time.sleep(2)
try:
    for i in range(1, 100):
        emoji = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/div[1]/div/div/div[3]/div[1]/ul/li[{0}]/div'.format(i))

        emoji_title = emoji.get_attribute('title')
        emoji_title = emoji_title[1:-1]
        emoji_style = emoji.get_attribute('style')
        emoji_link = 'https:' + emoji_style.split('"')[1]

        print(emoji_title)
        print(emoji_link)
        print()
        content = requests.get(emoji_link).content
        with open('bilibili_emoji/tv/{0}.png'.format(emoji_title), 'wb') as f:
            f.write(content)
            f.close()
except Exception as e:
    print(e)