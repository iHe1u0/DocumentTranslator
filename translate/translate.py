import requests
import hashlib
import random
import json

host = "https://fanyi-api.baidu.com/api/trans/vip/translate"

salt = random.randint(19991124, 20080412)


class Translator:
    def __init__(self) -> None:
        pass

    def translate(self, text,  sourceLang="zh", toLang="en"):
        if not isinstance(text, str):
            return text
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        params = {
            "q": text,
            "from": sourceLang,
            "to": toLang,
            "appid": appid,
            "salt": str(salt),
            "sign": self.genearteMD5(appid+text+str(salt)+key)
        }
        request_result = requests.post(
            url=host, headers=headers, params=params)
        translate_result = json.loads(request_result.text)
        return translate_result["trans_result"][0]["dst"]

    def genearteMD5(self, text):
        hl = hashlib.md5()
        hl.update(text.encode(encoding='utf-8'))
        return hl.hexdigest()
