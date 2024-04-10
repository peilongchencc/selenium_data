from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 设置你的web driver的路径和选项
driver_path = './chromedriver'  # 替换为你的驱动路径
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # 无头模式，没有GUI

# 启动Selenium WebDriver
driver = webdriver.Chrome(driver_path, options=options)

# 打开京东网站
driver.get('https://www.jd.com')

# 在搜索框中输入商品名称并搜索
search_box = driver.find_element(By.ID, 'key')
search_box.send_keys('你想搜索的商品名称')  # 替换为你想搜索的商品名称
search_box.send_keys(Keys.ENTER)

# 等待页面加载
driver.implicitly_wait(10)  # 等待时间根据网页响应时间而定

# 抓取商品信息
products = driver.find_elements(By.CLASS_NAME, 'gl-item')
for product in products:
    # 获取商品标题和价格等信息
    title = product.find_element(By.CLASS_NAME, 'p-name').text
    price = product.find_element(By.CLASS_NAME, 'p-price').text
    print(f'Title: {title}, Price: {price}')

# 关闭浏览器
driver.quit()
