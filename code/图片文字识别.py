# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import recognition
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

client = recognition.recog()

### 输入图片所在网址
id = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1595997016689&di=bca7813c423c3a35c571c17e14ff4efd&imgtype=0&src=http%3A%2F%2Fimg.bjtata.com%2Fimg%2F2d5d5b783b2afc6e.jpg"
image = requests.get(id).content
res = client.basicGeneral(image)
for i in range(len(res['words_result'])):
    print(res['words_result'][i]['words'])