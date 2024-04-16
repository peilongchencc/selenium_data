"""
File path:fetch_webpage_content_baidu_top10.py
Author: peilongchencc@163.com
Description: 通过selenium 4获取百度热搜top10, 包括文本和跳转链接。跳转链接是百度搜索引擎界面,不是具体的热点信息界面。
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
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from loguru import logger

# 设置日志
logger.remove()
logger.add("baidu_hot_search.log", rotation="1 GB", backtrace=True, diagnose=True, format="{time} {level} {message}")

def fetch_webpage_content(url):
    """通过selenium 4获取网页的标题和内容及链接。
    Args:
        url: 网页链接
    Returns:
        title, items: 网页标题,包含文本和链接的列表。
    Notes:
        1. 运行前需要先分析并修改函数中的xpath,确保xpath对应的是自己需要抓取的内容。
    """
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')

        # 实例化 WebDriver
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        
        # 等待元素加载
        driver.implicitly_wait(5)
        
        # 抓取标题
        title = driver.title
        
        # 抓取内容和链接
        items = []
        try:
            elements = driver.find_elements(By.XPATH, '//ul[@id="hotsearch-content-wrapper"]/li/a')
            for element in elements:
                item_text = element.text
                item_href = element.get_attribute('href')  # 获取href属性
                items.append({'text': item_text, 'href': item_href})
        except NoSuchElementException:
            # 当元素未找到时记录错误信息
            logger.error("未找到热点话题对应元素。")

        # 找到 "换一换" 按钮并点击
        refresh_button = driver.find_element(By.ID, "hotsearch-refresh-btn")
        refresh_button.click()

        # 针对 "换一换" 后的热搜,获取后续的热搜。
        try:
            elements = driver.find_elements(By.XPATH, '//ul[@id="hotsearch-content-wrapper"]/li/a')
            for element in elements:
                item_text = element.text
                item_href = element.get_attribute('href')
                items.append({'text': item_text, 'href': item_href})
        except NoSuchElementException:
            # 当元素未找到时记录错误信息
            logger.error("在点击'换一换'后, 未找到热点话题对应元素。")
            
    except WebDriverException as e:
        title, items = None, [{"error": "在使用Selenium时发生错误:{}".format(str(e))}]
    
    finally:
        # 确保无论如何都关闭浏览器
        if driver:
            driver.quit()
    
    return title, items

if __name__ == "__main__":
    url = 'https://www.baidu.com/'
    title, items = fetch_webpage_content(url)
    logger.info(f"Title: {title}")
    for item in items:
        logger.info(f"Text: {item['text']} - Href: {item['href']}")
    logger.info(f"\n")