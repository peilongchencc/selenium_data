from urllib.parse import urlparse, urlunparse

def ensure_https(url):
    """检查一个 URL 是否包含协议，并在没有协议的情况下添加 "https://"。
    """
    # 解析URL
    parsed_url = urlparse(url)

    # 检查是否有协议 (即scheme部分)
    if not parsed_url.scheme:
        # 如果没有协议，添加'https://'
        new_url = urlunparse(('https', parsed_url.netloc, parsed_url.path, parsed_url.params, parsed_url.query, parsed_url.fragment))
        # 如果 netloc 是空的，可能是因为原始 URL 只是一个路径部分，没有域名
        if not parsed_url.netloc:
            new_url = 'https://' + url
        return new_url

    # 如果已有协议，直接返回原URL
    return url

if __name__ == '__main__':
    # 测试用例
    urls = [
        "www.example.com",
        "https://www.example.com",
        "http://www.example.com",
        "example.com/path?query=123",
        "//www.example.com",  # 这种情况也会被处理
    ]

    for test_url in urls:
        print(ensure_https(test_url))
