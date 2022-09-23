# 清华大学开源镜像站日志解析
# 日志文件为 data/tuna-log.py
# 其他 nginx 日志同理
import re

pattern = re.compile(
    r'(?P<fake_remote_addr>.*?) - (?P<remote_user>.*?) \[(?P<time_local>.*?)] "(?P<request>.*?)" (?P<status>.*?) '
    r'(?P<body_bytes_sent>.*?) "(?P<sent_http_content_type>.*?)" "(?P<http_referer>.*?)" "(?P<http_user_agent>.*?)"'
    r' - (?P<scheme>.*?)\n')

with open('data/tuna-log.log') as f:
    for line in f:
        res = re.match(pattern, line)
        print(res.groupdict())
