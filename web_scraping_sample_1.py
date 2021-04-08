# Windows10 Python3.9

# インポート
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import pandas as pd

# Chromedriverのインストールとパスの取得
chrome_path = ChromeDriverManager().install()

# ブラウザを起動
# browser = webdriver.Chrome(chrome_path)

# ブラウザを非表示で起動
options = Options()
options.add_argument('--headless')
browser = webdriver.Chrome(chrome_path, options=options)
print("Chromeを非表示で起動")

# Webスクレイピング入門のログインページにアクセス
url = 'https://scraping-for-beginner.herokuapp.com/login_page'
browser.get(url)
print("ログインページにアクセス")

# 1秒待機
sleep(1)

print("ログイン処理")
# username を入力
element_username = browser.find_element_by_id('username')
element_username.send_keys('imanishi')

# password を入力
element_password = browser.find_element_by_id('password')
element_password.send_keys('kohei')

# ログインボタンをクリック
element_login_btn = browser.find_element_by_id('login-btn')
element_login_btn.click()

print("テーブル情報を取得")
# th
elements_th = browser.find_elements_by_tag_name('th')
keys = []
for element_th in elements_th:
    key = element_th.text
    keys.append(key)
    
# td
elements_td = browser.find_elements_by_tag_name('td')
values = []
for element_td in elements_td:
    value = element_td.text
    values.append(value)

print("データフレーム化")
# データフレーム
df = pd.DataFrame()

df['項目'] = keys
df['値'] = values

print("CSVで保存")
# CSVで保存
df.to_csv('講師情報.csv', index=False)

print("Chromeを終了")
# ブラウザを閉じる
browser.quit()

print('実行終了')
