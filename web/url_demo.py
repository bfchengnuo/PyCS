from urllib import parse

domain = "https://bfchengnuo.com"
print(parse.urljoin(domain, "/dev/echo"))
print(parse.urljoin(domain, "dev/echo"))
# 已存在，不会再做处理
print(parse.urljoin(domain, "https://baidu.com/dev/echo"))