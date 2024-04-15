import os
import re
import subprocess

from selenium import webdriver


def test_basic_options():
    """
    Starting a Chrome session with basic defined options looks like this:

    使用基本定义的选项启动Chrome会话如下所示:
    """
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)

    driver.quit()


def test_args():
    """
    参数:
    
    The args parameter is for a list of command line switches to be used when starting the browser.

    args参数用于启动浏览器时使用的一系列命令行开关。

    There are two excellent resources for investigating these arguments:

    有两个优秀的资源可供调查这些参数：

    - Chrome Flags for Tooling(用于工具的Chrome标志)

    - List of Chromium Command Line Switches(Chromium命令行开关列表)

    Commonly used args include `--start-maximized`, `--headless=new` and `--user-data-dir=` ...

    常用的参数包括 `--start-maximized` , `--headless=new` 和 `--user-data-dir=` ...
    """
    options = webdriver.ChromeOptions()

    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    driver.get('http://selenium.dev')

    driver.quit()


def test_set_browser_location(chrome_bin):
    """
    Start browser in a specified location(通过指定位置启动浏览器):

    The binary parameter takes the path of an alternate location of browser to use.

    二进制参数接受要使用的浏览器备用位置的路径。

    With this parameter you can use chromedriver to drive various Chromium based browsers.

    使用此参数,您可以使用chromedriver驱动各种基于Chromium的浏览器。

    Add a browser location to options(向选项中添加浏览器位置):
    """
    options = webdriver.ChromeOptions()

    options.binary_location = chrome_bin

    driver = webdriver.Chrome(options=options)

    driver.quit()


def test_add_extension():
    """
    Add extensions(添加扩展):

    The `extensions` parameter accepts crx files.
    
    `extensions` 参数接受crx文件。

    As for unpacked directories, please use the `load-extension` argument instead.
    
    至于解压的目录,请使用 `load-extension` 参数。

    Add an extension to options(向选项中添加一个扩展):
    """
    options = webdriver.ChromeOptions()
    extension_file_path = os.path.abspath("tests/extensions/webextensions-selenium-example.crx")

    options.add_extension(extension_file_path)

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.selenium.dev/selenium/web/blank.html")

    driver.quit()


def test_keep_browser_open():
    """
    Keeping browser open(保持浏览器打开):

    Setting the `detach` parameter to true will keep the browser open after the process has ended, 
    so long as the quit command is not sent to the driver.
    
    将 `detach` 参数设置为true将在进程结束后保持浏览器打开,只要没有向驱动程序发送quit命令。
    """
    options = webdriver.ChromeOptions()

    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)
    driver.get('http://selenium.dev')

    driver.quit()


def test_exclude_switches():
    """
    Excluding arguments(排除参数):

    Chromedriver has several default arguments it uses to start the browser.
    
    Chromedriver有几个默认参数用于启动浏览器。

    If you do not want those arguments added, pass them into `excludeSwitches`.
    
    如果您不希望添加这些参数,请将它们传递给 `excludeSwitches`。

    A common example is to turn the popup blocker back on.
    
    一个常见的例子是重新启用弹出窗口拦截器。

    A full list of default arguments can be parsed from the Chromium Source Code.
    
    可以从Chromium源代码中解析出完整的默认参数列表。

    Set excluded arguments on options:
    在选项上设置排除的参数：
    """
    options = webdriver.ChromeOptions()

    options.add_experimental_option('excludeSwitches', ['disable-popup-blocking'])

    driver = webdriver.Chrome(options=options)
    driver.get('http://selenium.dev')

    driver.quit()


def test_log_to_file(log_path):
    """
    File output(文件输出)

    To change the logging output to save to a specific file(要将日志输出更改为保存到特定文件):
    """
    service = webdriver.ChromeService(log_output=log_path)

    driver = webdriver.Chrome(service=service)

    with open(log_path, 'r') as fp:
        assert "Starting ChromeDriver" in fp.readline()

    driver.quit()


def test_log_to_stdout(capfd):
    service = webdriver.ChromeService(log_output=subprocess.STDOUT)

    driver = webdriver.Chrome(service=service)

    out, err = capfd.readouterr()
    assert "Starting ChromeDriver" in out

    driver.quit()


def test_log_level(capfd):
    service = webdriver.ChromeService(service_args=['--log-level=DEBUG'], log_output=subprocess.STDOUT)

    driver = webdriver.Chrome(service=service)

    out, err = capfd.readouterr()
    assert '[DEBUG]' in err

    driver.quit()


def test_log_features(log_path):
    service = webdriver.ChromeService(service_args=['--append-log', '--readable-timestamp'], log_output=log_path)

    driver = webdriver.Chrome(service=service)

    with open(log_path, 'r') as f:
        assert re.match(r"\[\d\d-\d\d-\d\d\d\d", f.read())

    driver.quit()


def test_build_checks(capfd):
    service = webdriver.ChromeService(service_args=['--disable-build-check'], log_output=subprocess.STDOUT)

    driver = webdriver.Chrome(service=service)

    expected = "[WARNING]: You are using an unsupported command-line switch: --disable-build-check"
    out, err = capfd.readouterr()
    assert expected in err

    driver.quit()