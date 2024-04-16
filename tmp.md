```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from loguru import logger

class WebSeleniumBase:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')

        try:
            self.driver = webdriver.Chrome(options=options)
        except WebDriverException as e:
            logger.error(f"在使用Selenium时发生错误：{str(e)}")
            raise e  # 提前终止，如果webdriver启动失败

    def fetch_webpage_content(self, url):
        """这个方法应由子类实现具体逻辑"""
        raise NotImplementedError("This method should be overridden by subclasses")

    def close_driver(self):
        if self.driver:
            self.driver.quit()

class BaiduScraper(WebSeleniumBase):
    def fetch_webpage_content(self, url):
        try:
            self.driver.get(url)
            self.driver.implicitly_wait(5)
            title = self.driver.title
            items = self._fetch_hot_search()
        except WebDriverException as e:
            logger.error(f"在使用Selenium时发生错误：{str(e)}")
            return None, []
        finally:
            self.close_driver()

        return title, items

    def _fetch_hot_search(self):
        items = []
        try:
            elements = self.driver.find_elements(By.XPATH, '//ul[@id="hotsearch-content-wrapper"]/li/a')
            for element in elements:
                item_text = element.text
                item_href = element.get_attribute('href')
                items.append({'text': item_text, 'href': item_href})
            
            refresh_button = self.driver.find_element(By.ID, "hotsearch-refresh-btn")
            refresh_button.click()

            elements = self.driver.find_elements(By.XPATH, '//ul[@id="hotsearch-content-wrapper"]/li/a')
            for element in elements:
                item_text = element.text
                item_href = element.get_attribute('href')
                items.append({'text': item_text, 'href': item_href})
        except NoSuchElementException as e:
            logger.error(f"元素未找到: {str(e)}")
        except WebDriverException as e:
            logger.error(f"在点击'换一换'后, 发生错误: {str(e)}")
        
        return items
```