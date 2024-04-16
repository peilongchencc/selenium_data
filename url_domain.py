from urllib.parse import urlparse

def extract_domain_from_url(url):
    """解析URL以获取域名。
    Args:
        url(str)
    Return:
        domain(str):网址域名。
    Example:
        "https://baijiahao.baidu.com/s?id=1793832549445442560" --> "baijiahao.baidu.com"
        "https://www.zhihu.com/question/36809525/answer/1928922951" --> "www.zhihu.com"
    """
    # 解析URL以获取域名
    domain = urlparse(url).netloc
    return domain