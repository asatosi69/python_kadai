import time                            # スリープを使うために必要
from selenium import webdriver         # Webブラウザを自動操作する（python -m pip install selenium)
driver = webdriver.Chrome('./chromedriver.exe')
driver.get('https://www.google.com/')  # Googleを開く
time.sleep(5)                          # 5秒間待機
driver.quit()    
