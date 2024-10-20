import requests

# 代理服务器的地址和端口
# proxy_server = '45.88.230.16'
# proxy_port = 7879

# 创建一个请求会话，并设置代理
session = requests.Session()
# session.proxies = {
#     'http': f'http://{proxy_server}:{proxy_port}',
#     'https': f'https://{proxy_server}:{proxy_port}',
# }
#
# # 发送请求
response = requests.get('https://127.0.0.1')

# 打印响应内容
print(response.text)
