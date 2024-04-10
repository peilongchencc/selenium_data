"""
File path:fetch_webpage_content_contain_images.py
Author: peilongchencc@163.com
Description: 异步方式通过selenium 4获取网页的标题和内容(同时下载图片)。
Requirements: 
1. pip install selenium aiofiles aiohttp
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
import asyncio
import aiohttp
import aiofiles
from urllib.parse import urlparse
import os

async def download_image(image_url):
    """异步下载图片
    Args:
        image_url: 图片链接(单个),由于是异步下载,故此处不需要考虑是否为单个或多个。
    Return:
        下载图片,无返回值。
    Notes:
        当前函数使用前需要先分析并修改函数中的 `clear_url` 部分,确保图片链接提取正确。
    """
    try:
        # 清洗URL
        clean_url = image_url.split('@')[0]
        # 从 URL 路径中直接提取文件名
        parsed_url = urlparse(clean_url)
        
        # 定义文件保存路径
        filename = parsed_url.path.split('/')[-1]
        save_path = f"docs/pictures/{filename}"
        # 获取给定路径中的路径名，例如对于 f"ocr_pictures/{filename}" 会返回 "ocr_pictures"
        save_dir = os.path.dirname(save_path)
        
        # 检查保存路径是否存在，不存在则创建
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        async with aiohttp.ClientSession() as session:
            async with session.get(clean_url) as response:
                if response.status == 200:
                    # 使用 aiofiles 异步写文件
                    async with aiofiles.open(save_path, mode='wb') as f:
                        await f.write(await response.read())
                        print(f"图片已保存到 {save_path}")
                else:
                    print(f"下载图片失败，URL：{clean_url}，状态码：{response.status}")
    except Exception as e:
        print(f"在下载图片时发生错误：{str(e)}")

async def fetch_webpage_content(url):
    """通过selenium 4获取网页的标题和内容(包括图片)。
    Args:
        url: 网页链接
    Returns:
        title, text: 网页标题,网页内容。
    Notes:
        1. 运行前需要先分析并修改函数中的xpath,确保xpath对应的是自己需要抓取的内容。
        2. 由于selenium操作是阻塞的,在图片URLs收集完成后关闭浏览器,然后开始异步下载图片,这样可以避免长时间持有浏览器资源。
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

        # 尝试抓取图片
        try:
            image_elements = driver.find_elements(By.CSS_SELECTOR, "img._1g4Ex._1i_Oe")
            image_urls = [img.get_attribute('src') for img in image_elements]
        except NoSuchElementException:
            image_urls = []
            print("图片元素未找到")
        
        # 关闭浏览器
        driver.quit()

        if image_urls:
            # 不使用`asyncio.get_event_loop()`,方便作为模块集成到项目中。
            await asyncio.gather(*[download_image(url) for url in image_urls])
        else:
            print("没有找到图片URLs进行下载")
            
    except WebDriverException as e:
        title, text = None, None
        print(f"在使用Selenium时发生错误：{str(e)}")

    return title, text

if __name__ == "__main__":
    url = 'https://baijiahao.baidu.com/s?id=1793832549445442560'
    # 使用asyncio.run()启动主程序
    title, text = asyncio.run(fetch_webpage_content(url))
    print("Title:", title)
    print("Content:", text)