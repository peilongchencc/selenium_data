"""
File path:fetch_webpage_content.py
Author: peilongchencc@163.com
Description: 通过selenium 4获取网页的标题和内容。
Requirements: 
1. pip install selenium 
2. 查看自己的chrome版本
3. 安装与自己的chrome版本对应的chrome driver
Reference Link: 
Notes: 
1. selenium更新频繁且会改动函数名,如果代码无法报错,大概率是selenium版本不对,需要调整代码或selenium版本。
2. 笔者使用的selenium版本为 `selenium 4.18.1`。
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException

def fetch_webpage_content(url):
    """通过selenium 4获取网页的标题和内容。
    Args:
        url: 网页链接
    Returns:
        title, text: 网页标题,网页内容。
    Notes:
        1. 运行前需要先分析并修改函数中的xpath,确保xpath对应的是自己需要抓取的内容。
    """
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # 让浏览器在无头模式下运行（不显示界面）
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        
        # 实例化 WebDriver
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        
        # 等待元素加载
        driver.implicitly_wait(5)
        
        # 抓取标题(语法为selenium内置,无需修改)
        title = driver.title
        
        # 尝试抓取内容
        try:
            content = driver.find_element(By.CLASS_NAME, "_18p7x")
            text = content.text
        except NoSuchElementException:
            text = "内容元素未找到"

        # 关闭浏览器
        driver.quit()
            
    except WebDriverException as e:
        title, text = None, None
        print(f"在使用Selenium时发生错误：{str(e)}")

    return title, text

if __name__ == "__main__":
    url = 'https://baijiahao.baidu.com/s?id=1793832549445442560'
    title, text = fetch_webpage_content(url)
    print("Title:", title)
    print("Content:", text)