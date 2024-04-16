from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from loguru import logger

class WebSeleniumBase:
    def __init__(self):
        try:
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')  # 让浏览器在无头模式下运行（不显示界面）
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--no-sandbox')
            
            # 实例化 WebDriver
            self.driver = webdriver.Chrome(options=options)
        except WebDriverException as e:
            logger.error(f"在使用Selenium时发生错误：{str(e)}")
            
            # 确保无论如何都关闭浏览器
            if self.driver:
                self.driver.quit()
                
    def fetch_webpage_content(self, url):
        try:
            self.driver.get(url)
            
            # 等待元素加载(隐式等待)
            self.driver.implicitly_wait(5)
            
            # 抓取标题(语法为selenium内置,无需修改)
            title = self.driver.title
            
            # 尝试抓取内容
            try:
                content = self.driver.find_element(By.CLASS_NAME, "_18p7x")
                text = content.text
            except NoSuchElementException:
                logger.error("text内容元素未找到")
                
        except WebDriverException as e:
            title, text = None, None
            logger.error(f"在使用Selenium时发生错误：{str(e)}")

        finally:
            # 确保无论如何都关闭浏览器
            if self.driver:
                self.driver.quit()

        return title, text

    def fetch_baidu_hot_search_top10(self):
        try:
            self.driver.get(url)
            
            # 等待元素加载
            self.driver.implicitly_wait(5)
            
            # 抓取标题
            title = self.driver.title
            
            # 抓取内容和链接
            items = []
            try:
                elements = self.driver.find_elements(By.XPATH, '//ul[@id="hotsearch-content-wrapper"]/li/a')
                for element in elements:
                    item_text = element.text
                    item_href = element.get_attribute('href')  # 获取href属性
                    items.append({'text': item_text, 'href': item_href})
            except NoSuchElementException:
                # 当元素未找到时记录错误信息
                logger.error("未找到热点话题对应元素。")

            # 找到 "换一换" 按钮并点击
            refresh_button = self.driver.find_element(By.ID, "hotsearch-refresh-btn")
            refresh_button.click()

            # 针对 "换一换" 后的热搜,获取后续的热搜。
            try:
                elements = self.driver.find_elements(By.XPATH, '//ul[@id="hotsearch-content-wrapper"]/li/a')
                for element in elements:
                    item_text = element.text
                    item_href = element.get_attribute('href')
                    items.append({'text': item_text, 'href': item_href})
            except NoSuchElementException:
                # 当元素未找到时记录错误信息
                logger.error("在点击'换一换'后, 未找到热点话题对应元素。")
            
        except WebDriverException as e:
            title, items = None, [{"error": "在使用Selenium时发生错误:{}".format(str(e))}]
        return title, items
        

if __name__ == "__main__":
    selenium_server = WebSeleniumBase()
    url = 'https://baijiahao.baidu.com/s?id=1793832549445442560'
    title, text = selenium_server.fetch_webpage_content(url)
    print("Title:", title)
    print("Content:", text)