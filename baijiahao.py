from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
# 添加无头模式选项
options.add_argument('--headless')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=options)

url='https://baijiahao.baidu.com/s?id=1793832549445442560'
driver.get(url)

driver.implicitly_wait(5)

title = driver.title
print(title)

# 抓取所有内容(文字+图片)
content = driver.find_element(By.CLASS_NAME, "_18p7x")

text = content.text
print(text)

driver.quit()