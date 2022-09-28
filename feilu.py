# 飞卢小说数据抓取
import re

import requests


def pages():
    yield from (f"https://b.faloo.com/y_0_{i + 1}.html" for i in range(10))


pattern = re.compile(
    r'<h1 class="fontSize17andHei" title=".*? target="_blank" '
    r'title="(?P<name>.*?)">.*?</a></h1>.*?ontSize14andHui"><a.*?html" '
    r'title="(?P<type>.*?)" target="_blank".*?<span>'
    r"周点击：(?P<click>.*?)</span>.*?字数：(?P<count>.*?)</span>.*?"
    r'日期：<font class="fontSize14andChen"><font color="#ff6600">(?P<date>.*?)</font>'
)
for page in pages():
    r = requests.get(page)
    text = r.content.decode("gbk")
    result = pattern.finditer(text)
    for i in result:
        print(i.groupdict())
