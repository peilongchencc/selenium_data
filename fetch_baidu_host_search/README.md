# fetch baidu host search

## 爬取百度热搜前五:

从baidu主页爬取热搜前五，注意:百度主页处于未登录状态。<br>

目录                                     |用途                                                 |备注
----------------------------------------|----------------------------------------------------|---
fetch_webpage_content_baidu.py          | 通过selenium 4获取百度热搜。                          | 
fetch_baidu_hot_search.sh               | 以shell脚本形式运行爬取百度热搜的python代码             | 

## crontab运行该shell脚本:

```bash
# 每隔5分钟爬取百度热搜
*/5 * * * * /data/selenium_data/fetch_baidu_hot_search.sh >> /data/selenium_data/task_log.log 2>&1
```

每隔5分钟执行一次指定的脚本来爬取百度热搜信息，并将执行过程中产生的所有输出（包括可能的错误信息）追加到日志文件中。<br>

笔者代码中添加了log，故在程序运行过程中shell脚本的log会输出到 `task_log.log` 文件，程序(例如 `fetch_webpage_content_baidu.py` )中的log会输出到 `baidu_hot_search.log` 文件。<br>