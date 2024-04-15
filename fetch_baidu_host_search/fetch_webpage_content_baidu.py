"""
File path:fetch_webpage_content_baidu.py
Author: peilongchencc@163.com
Description: 通过selenium 4获取百度热搜。
Requirements: 
1. pip install selenium 
2. 查看自己的chrome版本
3. 安装与自己的chrome版本对应的chrome driver
Reference Link: 
Notes: 
1. selenium更新频繁且会改动函数名,如果代码无法执行,大概率是selenium版本不对,需要调整代码或selenium版本。
2. 笔者使用的selenium版本为 `selenium 4.18.1`。
Todo:
1. 未触发百度主页ip封禁策略,ip池未添加。
2. 利用aiomysql以异步的方式将抓取到的热搜写入mysql,较少程序耗时。写入mysql时注意去重,一段时间内的热搜可能是不变的。
3. 当前抓取的百度主页热搜前5的内容,从第6位开始需要点击百度主页热搜的 "换一换" 按钮进行切换,代码中暂未添加该逻辑(笔者还不了解selenium怎么处理按键点击)。
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from loguru import logger

# 设置日志
logger.remove()
logger.add("baidu_hot_search.log", rotation="1 GB", backtrace=True, diagnose=True, format="{time} {level} {message}")

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
        
        # 等待元素加载(隐式等待)
        driver.implicitly_wait(5)
        
        # 抓取标题(语法为selenium内置,无需修改)
        title = driver.title
        
        # 抓取内容
        text_elements = []
        try:
            elements = driver.find_elements(By.XPATH, '//ul[@id="hotsearch-content-wrapper"]/li/a')
            for element in elements:
                text_elements.append(element.text)
        except NoSuchElementException:
            text_elements = ["内容元素未找到"]
            
    except WebDriverException as e:
        title, text_elements = None, ["在使用Selenium时发生错误:{}".format(str(e))]
    
    finally:
        # 确保无论如何都关闭浏览器
        if driver:
            driver.quit()
    return title, text_elements

if __name__ == "__main__":
    url = 'https://www.baidu.com/'
    title, text_elements = fetch_webpage_content(url)
    logger.info(f"Title:{title}")
    for text in text_elements:
        logger.info(f"Content:{text}")
    logger.info(f"\n")