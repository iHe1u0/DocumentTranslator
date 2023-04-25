import requests
import hashlib
import random
import json

host = "https://fanyi-api.baidu.com/api/trans/vip/translate"

salt = random.randint(19991124, 20080412)


def _generate_md5(text):
    return hashlib.md5(text.encode('utf-8')).hexdigest()


def _is_digital(string):
    if string is None:
        return False
    if (string is int) or (string is float):
        return True
    else:
        try:
            int(string)
            float(string)
        except ValueError:
            return False
    return True


class BaiduTranslator:
    def __init__(self, app_id, key):
        self.api_id = app_id
        self.api_key = key

    def translate(self, text, source_lang="auto", des_lang="zh"):
        if text is None:
            return ''
        if _is_digital(text):
            return text
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        params = {
            "q": text,
            "from": source_lang,
            "to": des_lang,
            "appid": self.api_id,
            "salt": str(salt),
            "sign": _generate_md5(self.api_id + text + str(salt) + self.api_key)
        }
        request_result = requests.post(
            url=host,
            headers=headers,
            params=params
        )
        result_text = request_result.text
        if result_text.startswith('{"error_code'):
            return text
        translate_result = json.loads(result_text)
        return translate_result["trans_result"][0]["dst"]
