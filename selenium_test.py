from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# 设置Chrome选项以运行无头模式
options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")  # 确保无界面
# chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
# chrome_options.add_argument("--disable-dev-shm-usage")  # overcome limited resource problems

# 初始化WebDriver，使用webdriver_manager自动获取匹配的ChromeDriver
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

title = driver.title

# 设置隐式等待
driver.implicitly_wait(0.5)

# 定位元素
text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

# 执行操作
text_box.send_keys("Selenium")
submit_button.click()

# 获取结果
message = driver.find_element(by=By.ID, value="message")
text = message.text

# 关闭WebDriver
driver.quit()

# 打印结果
print(text)