# selenium:
- [selenium:](#selenium)
  - [Introduce-The Selenium Browser Automation Project(Selenium 浏览器自动化项目):](#introduce-the-selenium-browser-automation-projectselenium-浏览器自动化项目)
  - [WebDriver:](#webdriver)
    - [Write your first Selenium script:](#write-your-first-selenium-script)
      - [Eight Basic Components(八个基本组件):](#eight-basic-components八个基本组件)
        - [1. Start the session(开始会话)](#1-start-the-session开始会话)
        - [2. Take action on browser(在浏览器上执行操作)](#2-take-action-on-browser在浏览器上执行操作)
        - [3. Request browser information(请求浏览器信息)](#3-request-browser-information请求浏览器信息)
        - [4. Establish Waiting Strategy(建立等待策略)](#4-establish-waiting-strategy建立等待策略)
        - [5. Find an element(查找元素):](#5-find-an-element查找元素)
        - [6. Take action on element(对元素执行操作):](#6-take-action-on-element对元素执行操作)
        - [7. Request element information(请求元素信息):](#7-request-element-information请求元素信息)
        - [8. End the session(结束会话):](#8-end-the-session结束会话)
      - [Whole Code(完整代码):](#whole-code完整代码)
  - [Common use cases of Selenium(Selenium的常见用途):](#common-use-cases-of-seleniumselenium的常见用途)
    - [Web Repetitive Tasks(网页重复任务):](#web-repetitive-tasks网页重复任务)
    - [Web Scraping(网页抓取):](#web-scraping网页抓取)
  - [Chrome specific functionality(Chrome特定功能):](#chrome-specific-functionalitychrome特定功能)
    - [Options(选项):](#options选项)
  - [selenium示例:](#selenium示例)
  - [selenium使用示例(异步):](#selenium使用示例异步)

## Introduce-The Selenium Browser Automation Project(Selenium 浏览器自动化项目):

Selenium is an umbrella project for a range of tools and libraries that enable and support the automation of web browsers.<br>

> 在 "an umbrella project" 中，"umbrella" 的意思是“伞”，在这里是比喻性地指代一个项目或组织，它下面涵盖了多个相关的子项目或组成部分。因此，"an umbrella project" 指的是一个项目或组织，它作为一个整体，覆盖了多个相关的子项目或组成部分。

Selenium 是一个涵盖一系列工具和库的项目，旨在支持和实现对 Web 浏览器的自动化。<br>

It provides extensions(扩展;延伸) to emulate(模仿;模拟) user interaction(交互) with browsers, a distribution server for scaling(扩展性;可伸缩性) browser allocation, and the infrastructure for implementations of the W3C WebDriver specification that lets you write interchangeable code for all major web browsers.<br>

> "distribution": “分发”或“分配”。它指的是 Selenium 提供的服务器，用于分发或分配浏览器资源。

它提供了扩展功能，以模拟用户与浏览器的交互，一个用于扩展浏览器分配的分发服务器，以及实现 W3C WebDriver 规范的基础设施，让您可以为所有主要的 Web 浏览器编写可互换的代码。<br>

🔥🔥🔥This project is made possible by volunteer contributors who have put in thousands of hours of their own time, and made the source code freely available for anyone to use, enjoy, and improve.<br>

🔥🔥🔥这个项目得以实现，要感谢那些自愿贡献者，他们投入了数千小时的个人时间，并免费提供了源代码，供任何人使用、享受和改进。<br>

Selenium brings together browser vendors, engineers, and enthusiasts to further an open discussion around automation of the web platform. The project organises an annual conference to teach and nurture the community.<br>

Selenium 聚集了浏览器供应商、工程师和爱好者，促进了对 Web 平台自动化的开放讨论。该项目每年组织一次会议，旨在教育和培育社区。<br>

At the core of Selenium is [**WebDriver**](https://www.selenium.dev/documentation/webdriver/), an interface to write instruction sets that can be run interchangeably in many browsers. <br>

在 Selenium 的核心是 **WebDriver**，它是一个接口，用于编写可在许多浏览器中可互换运行的指令集。<br>

Once you’ve installed everything, only a few lines of code get you inside a browser. You can find a more comprehensive example in [**Writing your first Selenium script**](https://www.selenium.dev/documentation/webdriver/getting_started/first_script/).<br>

一旦您安装了所有内容，只需几行代码就可以进入一个浏览器。您可以在“编写您的第一个 Selenium 脚本”中找到一个更全面的例子。<br>

不同语言安装方式的链接如下:<br>

```txt
https://www.selenium.dev/downloads/
```

Python语言的安装方式如下:<br>

```bash
pip install selenium
```

```python
from selenium import webdriver


driver = webdriver.Chrome()

driver.get("http://selenium.dev")

driver.quit()
```

See the **Overview** to check the different project components and decide if Selenium is the right tool for you.<br>

请查看概述，检查不同的项目组件，并决定是否 Selenium 是适合您的正确工具。<br>

You should continue on to [**Getting Started**](https://www.selenium.dev/documentation/webdriver/getting_started/) to understand how you can install Selenium and successfully use it as a test automation tool, and scaling simple tests like this to run in large, distributed environments on multiple browsers, on several different operating systems.<br>

您应该继续查看入门指南，了解如何安装 Selenium 并成功将其用作测试自动化工具，以及如何将简单的测试扩展到在多个浏览器、多个不同操作系统的大型分布式环境中运行。<br>


## WebDriver:

If you are beginning with desktop website or mobile website test automation, then you are going to be using WebDriver APIs. <br>

如果你刚开始进行桌面网站或移动网站的测试自动化，那么你将会使用WebDriver API。<br>

WebDriver uses browser automation APIs provided by browser vendors(供应商) to control the browser and run tests. This is as if a real user is operating the browser. <br>

WebDriver利用浏览器供应商提供的浏览器自动化API来控制浏览器并运行测试。这就像一个真实的用户在操作浏览器一样。<br>

Since WebDriver does not require its API to be compiled with application code, it is not intrusive(侵入性的;打扰的). Hence, you are testing the same application which you push live.<br>

由于WebDriver不需要将其API与应用程序代码编译在一起，因此它不会对应用程序造成影响。因此，你正在测试的是发布的同一应用程序。<br>

If you are new to Selenium, we have a few resources that can help you get up to speed right away.<br>

如果你是Selenium的新手，我们有一些资源可以帮助你立即上手。<br>

Selenium supports automation of all the major browsers in the market through the use of WebDriver.<br>

Selenium通过WebDriver支持市场上所有主要的浏览器的自动化。<br>

WebDriver is an API and protocol(协议) that defines a language-neutral interface for controlling the behaviour of web browsers.<br>

WebDriver是一个API和协议，定义了一个语言中立的接口，用于控制浏览器的行为。<br>

Each browser is backed(支持) by a specific WebDriver implementation(实现), called a driver.<br>

每个浏览器都由一个特定的WebDriver实现支持，称为驱动程序。<br>

The driver is the component(组件) responsible for delegating(委派) down to the browser, and handles communication to and from Selenium and the browser.<br>

驱动程序是负责向浏览器委派任务，并处理Selenium与浏览器之间的通信的组件。<br>

This separation(分离) is part of a conscious(有意识的;意识到的) effort to have browser vendors take responsibility for the implementation for their browsers.<br>

这种分离是有意识的努力的一部分，旨在让浏览器供应商为其浏览器的实现负责。<br>

Selenium makes use of these third party drivers where possible, but also provides its own drivers maintained(维护;保持) by the project for the cases when this is not a reality(现实或实际情况).<br>

Selenium尽可能地利用这些第三方驱动程序，但也为那些无法实现的情况提供了由项目维护的自己的驱动程序。<br>

The Selenium framework ties(系;绑;连接) all of these pieces together through a user-facing interface that enables the different browser backends(后端) to be used transparently("透明地"或"清晰地"), enabling cross-browser and cross-platform automation.<br>

> 在文中，"transparently" 指的是以透明的方式或清晰的方式进行操作或执行某项任务，没有隐藏或复杂的过程。这表示 Selenium 框架使得不同浏览器后端可以被透明地使用，即用户无需关注底层细节，就可以实现跨浏览器和跨平台的自动化。

Selenium框架通过用户界面将所有这些部分联系在一起，使不同的浏览器后端可以清晰地使用，实现跨浏览器和跨平台的自动化。<br>

Selenium setup is quite different from the setup of other commercial(商业相关的) tools.<br>

Selenium的设置与其他商业工具的设置非常不同。<br>

🚀🚀🚀Before you can start writing Selenium code, you have to:<br>

🚀🚀🚀在你可以开始编写Selenium代码之前，你必须:<br>

- install the language bindings libraries for your language of choice(安装你选择的语言的语言绑定库)

- the browser you want to use(你想要使用的浏览器)

- the driver for that browser(该浏览器的驱动程序)

### Write your first Selenium script:

Step-by-step instructions(指示、说明或指导) for constructing(建造;构建) a Selenium script.<br>

逐步指南，构建 Selenium 脚本<br>

Once you have Selenium installed, you’re ready to write Selenium code.<br>

一旦你安装了 Selenium，你就可以开始编写 Selenium 代码了。<br>

#### Eight Basic Components(八个基本组件):

Everything Selenium does is send the browser commands to do something or send requests for information.<br>

Selenium 所做的一切都是发送浏览器命令来执行某些操作或发送请求获取信息。<br>

Most of what you’ll do with Selenium is a combination(组合) of these basic commands.<br>

你将使用 Selenium 大部分时间都是在组合这些基本命令。<br>

##### 1. Start the session(开始会话)

For more details on starting a session read our documentation on driver sessions.<br>

有关如何开始会话的更多详细信息，请阅读我们关于驱动程序会话的文档。<br>

```python
driver = webdriver.Chrome()
```

##### 2. Take action on browser(在浏览器上执行操作)

In this example we are navigating to a web page.<br>

在此示例中，我们正在导航到一个网页。<br>

```python
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
```

##### 3. Request browser information(请求浏览器信息)

There are a bunch of types of information about the browser you can request, including window handles, browser size / position, cookies, alerts, etc.<br>

您可以请求关于浏览器的各种类型的信息，包括窗口句柄、浏览器大小/位置、cookie、警报等。<br>

💦💦💦"窗口句柄"是操作系统为了管理窗口而分配给每个窗口的唯一标识符。在 Selenium 中，"window handles" 通常用于引用浏览器窗口的标识符，以便在多个窗口之间进行切换和操作。<br>

💦💦💦游客在使用网页浏览器时不会直接看到窗口句柄。窗口句柄是操作系统为了管理窗口而分配给每个窗口的唯一标识符，它通常在后台被使用。<br>

```python
title = driver.title
```

##### 4. Establish Waiting Strategy(建立等待策略)

Synchronizing(同步) the code with the current state of the browser is one of the biggest challenges with Selenium, and doing it well is an advanced topic.<br>

与当前浏览器状态同步代码是Selenium的最大挑战之一，良好地完成这项任务是一个高级主题。<br>

Essentially(基本上) you want to make sure that the element is on the page before you attempt to locate it and the element is in an interactable state before you attempt to interact with it.<br>

基本上，首先要确保元素出现在页面上后才尝试定位它，并且在尝试与其交互之前，元素处于可交互状态。<br>

An implicit wait is rarely the best solution, but it’s the easiest to demonstrate here, so we’ll use it as a placeholder.<br>

隐式等待很少是最佳解决方案，但它在这里是最容易演示的，因此我们将其用作占位符。<br>

[Read more about Waiting strategies](https://www.selenium.dev/documentation/webdriver/waits/).<br>

```python
driver.implicitly_wait(0.5)
```

🚨🚨🚨implicit wait 是一种等待策略，指定了在查找元素时等待的最长时间，如果在规定的时间内找不到元素，就会抛出异常。<br>

##### 5. Find an element(查找元素):

The majority of commands in most Selenium sessions are element related, and you can’t interact with one without first finding an element.<br>

大多数Selenium会话中的命令都与元素相关，而没有先找到元素，您无法与之交互。<br>

```python
text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
```

##### 6. Take action on element(对元素执行操作):

There are only a handful of actions to take on an element, but you will use them frequently.<br>

对元素执行的操作很少，但您会经常使用它们。<br>

> "Handful" 是一个名词，指的是一把手所能容纳的量，也可以用来形容一小部分、一些或一小批量的东西。在描述数量时，它通常意味着有限的、不多的数量，正好或几乎正好可以用一只手来握住或掌握。

```python
text_box.send_keys("Selenium")
submit_button.click()
```

##### 7. Request element information(请求元素信息):

Elements store a lot of information that can be requested.<br>

元素存储了很多可以请求的信息。<br>

```python
text = message.text
```

##### 8. End the session(结束会话):

This ends the driver process, which by default closes the browser as well. No more commands can be sent to this driver instance. See Quitting Sessions.<br>

这会结束驱动程序进程，默认情况下也会关闭浏览器。无法再向此驱动程序实例发送更多命令。请参阅退出会话。<br>

```python
driver.quit()
```

#### Whole Code(完整代码):

我的代码如下：

```python
# python selenium_test_code.py
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv

# 加载环境变量
dotenv_path = '.env.local'
load_dotenv(dotenv_path=dotenv_path)

# 设置网络代理环境变量
os.environ['http_proxy'] = os.getenv("HTTP_PROXY")
os.environ['https_proxy'] = os.getenv("HTTPS_PROXY")


driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

title = driver.title

driver.implicitly_wait(0.5)

text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

text_box.send_keys("Selenium")
submit_button.click()

message = driver.find_element(by=By.ID, value="message")
text = message.text

driver.quit()
```

终端信息：

```log
(langchain) root@iZ2zea5v77oawjy2qz7c20Z:/data/chat_system# python selenium_test_code.py 
Traceback (most recent call last):
  File "/data/chat_system/selenium_test_code.py", line 15, in <module>
    driver = webdriver.Chrome()
  File "/root/anaconda3/envs/langchain/lib/python3.10/site-packages/selenium/webdriver/chrome/webdriver.py", line 45, in __init__
    super().__init__(
  File "/root/anaconda3/envs/langchain/lib/python3.10/site-packages/selenium/webdriver/chromium/webdriver.py", line 61, in __init__
    super().__init__(command_executor=executor, options=options)
  File "/root/anaconda3/envs/langchain/lib/python3.10/site-packages/selenium/webdriver/remote/webdriver.py", line 208, in __init__
    self.start_session(capabilities)
  File "/root/anaconda3/envs/langchain/lib/python3.10/site-packages/selenium/webdriver/remote/webdriver.py", line 292, in start_session
    response = self.execute(Command.NEW_SESSION, caps)["value"]
  File "/root/anaconda3/envs/langchain/lib/python3.10/site-packages/selenium/webdriver/remote/webdriver.py", line 347, in execute
    self.error_handler.check_response(response)
  File "/root/anaconda3/envs/langchain/lib/python3.10/site-packages/selenium/webdriver/remote/errorhandler.py", line 229, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.SessionNotCreatedException: Message: session not created: Chrome failed to start: exited normally.
  (session not created: DevToolsActivePort file doesn't exist)
  (The process started from chrome location /usr/bin/google-chrome is no longer running, so ChromeDriver is assuming that Chrome has crashed.)
Stacktrace:
#0 0x557bb674e303 <unknown>
#1 0x557bb64332b7 <unknown>
#2 0x557bb6467b40 <unknown>
#3 0x557bb64636e5 <unknown>
#4 0x557bb64adabc <unknown>
#5 0x557bb64a1123 <unknown>
#6 0x557bb6471095 <unknown>
#7 0x557bb647209e <unknown>
#8 0x557bb67126ab <unknown>
#9 0x557bb67164ba <unknown>
#10 0x557bb66fef85 <unknown>
#11 0x557bb671712f <unknown>
#12 0x557bb66e2e6f <unknown>
#13 0x557bb673b5f8 <unknown>
#14 0x557bb673b7c2 <unknown>
#15 0x557bb674d4a4 <unknown>
#16 0x7fd2f12a16db start_thread

(langchain) root@iZ2zea5v77oawjy2qz7c20Z:/data/chat_system# 
```

## Common use cases of Selenium(Selenium的常见用途):

Most people use Selenium to execute(执行) automated(自动) tests for web applications, but Selenium supports any use case of browser automation.<br>

大多数人使用 Selenium 执行网页应用程序的自动化测试，但 Selenium 支持任何浏览器自动化的用例。<br>

### Web Repetitive Tasks(网页重复任务):

Perhaps you need to log into a website and download something, or submit a form. You can create a Selenium script to run with a service at preset(预设的、预先设定的) times.<br>

也许您需要登录到一个网站并下载一些内容，或者提交一个表单。您可以创建一个 Selenium 脚本，在预设时间与服务一起运行。<br>

### Web Scraping(网页抓取):

Are you looking to collect data from a site that doesn’t have an API?<br>

您是否想从没有 API 的网站收集数据？<br>

Selenium will let you do this, but please make sure you are familiar with the website’s terms of service as some websites do not permit it and others will even block(阻止;阻塞) Selenium.<br>

Selenium 将让您做到这一点，但请确保您熟悉网站的服务条款，因为一些网站不允许这样做，其他网站甚至会阻止 Selenium。<br>

## Chrome specific functionality(Chrome特定功能):

These are capabilities and features specific to Google Chrome browsers.<br>

这些是特定于Google Chrome浏览器的功能和特性。<br>

By default, Selenium 4 is compatible with Chrome v75 and greater. Note that the version of the Chrome browser and the version of chromedriver must match the major version.<br>

默认情况下，Selenium 4与Chrome v75及更高版本兼容。请注意，Chrome浏览器的版本和chromedriver的版本必须匹配主要版本。<br>

### Options(选项):

Capabilities common to all browsers are described on the Options page.<br>

适用于所有浏览器的功能被描述在选项页面上。<br>

Capabilities unique to Chrome and Chromium are documented at Google’s page for Capabilities & ChromeOptions.<br>

Chrome和Chromium独有的功能在Google的“能力和Chrome选项”页面上有文档记录。<br>

参数设置可参考以下内容:<br>

```python
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
```

Chrome完整Options用法详见下列网址:<br>

```txt
https://github.com/GoogleChrome/chrome-launcher/blob/main/docs/chrome-flags-for-tools.md
```

## selenium示例:

```python
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
1. selenium更新频繁且会改动函数名,如果代码无法执行,大概率是selenium版本不对,需要调整代码或selenium版本。
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
        
        # 等待元素加载(隐式等待)
        driver.implicitly_wait(5)
        
        # 抓取标题(语法为selenium内置,无需修改)
        title = driver.title
        
        # 尝试抓取内容
        try:
            content = driver.find_element(By.CLASS_NAME, "_18p7x")
            text = content.text
        except NoSuchElementException:
            text = "内容元素未找到"
            
    except WebDriverException as e:
        title, text = None, None
        print(f"在使用Selenium时发生错误：{str(e)}")

    finally:
        # 确保无论如何都关闭浏览器
        if driver:
            driver.quit()

    return title, text

if __name__ == "__main__":
    url = 'https://baijiahao.baidu.com/s?id=1793832549445442560'
    title, text = fetch_webpage_content(url)
    print("Title:", title)
    print("Content:", text)
```

🏝️🏝️🏝️Options解释:<br>

1. `options.add_argument('--headless')`
   - 这行代码添加了一个启动参数`'--headless'`到浏览器的启动选项中。当Chrome浏览器以`--headless`模式运行时，它不会显示用户界面（即无头模式）。这对于服务器环境或者需要自动化测试脚本在后台运行的情况非常有用，因为它不需要图形用户界面。

2. `options.add_argument('--disable-dev-shm-usage')`
   - 这行代码添加了`'--disable-dev-shm-usage'`参数，该参数会禁止Chrome使用`/dev/shm`，即共享内存。在某些系统或容器环境（如Docker）中，默认的共享内存很小，可能导致Chrome运行不稳定。通过禁用它的使用，Chrome会改用`/tmp`目录下的文件系统作为共享内存，虽然性能稍差，但更稳定。

3. `options.add_argument('--no-sandbox')`
   - 这行代码通过添加`'--no-sandbox'`参数，禁用了Chrome的沙箱模式。沙箱模式是一种安全机制，用于隔离运行中的进程，防止恶意软件或程序的破坏。在某些环境下，如Docker容器或者是特定的Linux系统中，启用沙箱模式可能会导致权限或兼容性问题。因此，在这些环境下，可能需要禁用沙箱来确保Chrome能够正常运行。但这样做可能会降低安全性，因此在不需要绕过这些限制的环境下不推荐使用。

这些选项一起使用时，允许Selenium以适合自动化测试的方式配置和启动Chrome浏览器，特别是在无图形用户界面的服务器环境中。<br>


## selenium使用示例(异步):

```python
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
1. selenium更新频繁且会改动函数名,如果代码无法执行,大概率是selenium版本不对,需要调整代码或selenium版本。
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
        
        # 等待元素加载(隐式等待)
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

    except WebDriverException as e:
        title, text = None, None
        print(f"在使用Selenium时发生错误：{str(e)}")

    finally:
        # 确保无论如何都关闭浏览器
        if driver:
            driver.quit()
    
    # 关闭浏览器后异步下载图片
    if image_urls:
        try:
            # 使用 return_exceptions=True 使得所有异常都被当作结果返回，而不是抛出
            # 不使用`asyncio.get_event_loop()`,方便作为模块集成到项目中。
            results = await asyncio.gather(*[download_image(url) for url in image_urls], return_exceptions=True)
            
            # 遍历结果，检查是否有异常被返回
            for result in results:
                if isinstance(result, Exception):
                    print(f"下载过程中发生异常：{result}")
        except Exception as e:
            # 这个异常处理是为了捕获gather本身的异常，通常是编程错误
            print(f"在异步下载图片时发生未预料的异常：{e}")
    else:
        print("没有找到图片URLs进行下载")

    return title, text

if __name__ == "__main__":
    url = 'https://baijiahao.baidu.com/s?id=1793832549445442560'
    # 使用asyncio.run()启动主程序
    title, text = asyncio.run(fetch_webpage_content(url))
    print("Title:", title)
    print("Content:", text)
```

当其他人调用笔者的代码时,请参考以下示例:<br>

```python
import asyncio

# 假设这是调用者的异步主函数
async def main():
    url = 'https://baijiahao.baidu.com/s?id=1793832549445442560'
    title, text = await fetch_webpage_content(url)
    print("Title:", title)
    print("Content:", text)

# 在调用者的代码中启动异步环境
if __name__ == "__main__":
    asyncio.run(main())
```