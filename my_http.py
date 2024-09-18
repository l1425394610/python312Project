import os
import requests
from datetime import datetime
import hmac
import hashlib
import base64
from urllib.parse import urlencode
# from sparkai.llm.llm import ChatSparkLLM, ChunkPrintHandler
# from sparkai.core.messages import ChatMessage

#星火认知大模型Spark Max的URL值，其他版本大模型URL值请前往文档（https://www.xfyun.cn/doc/spark/Web.html）查看
SPARKAI_URL = 'wss://spark-api.xf-yun.com/v3.5/chat'
#星火认知大模型调用秘钥信息，请前往讯飞开放平台控制台（https://console.xfyun.cn/services/bm35）查看
SPARKAI_APP_ID = 'f27b17f8'
SPARKAI_API_SECRET = 'OGJlMmMyNGVjMjc5YWUxOWZiMzA1M2I5'
SPARKAI_API_KEY = 'd95ec77058480acc1f1d6d3fcd0b541e'
#星火认知大模型Spark Max的domain值，其他版本大模型domain值请前往文档（https://www.xfyun.cn/doc/spark/Web.html）查看
SPARKAI_DOMAIN = 'generalv3.5'

def formatTime():
    now = datetime.now()

    # 格式化时间
    formatted_time = now.strftime('%a, %d %b %Y %H:%M:%S GMT')

    return formatted_time


if __name__ == "__main__":

    url = "https://spark-api-open.xf-yun.com/v1/chat/completions"
    data = {
        "model": "generalv3.5",  # 指定请求的模型
        "messages": [
            {
                "role": "user",
                "content": "你是谁"
            }
        ],
        "stream": True
    }
    header = {
        "Authorization": "Bearer MzGeYiHAtibtdSxAIFnY:RmbrbCTfuyRYJLDVwGEN"  # 注意此处替换自己的APIPassword
    }
    response = requests.post(url, headers=header, json=data, stream=True)

    # 流式响应解析示例
    response.encoding = "utf-8"
    for line in response.iter_lines(decode_unicode="utf-8"):
        print(line)

    # APIKey = "d95ec77058480acc1f1d6d3fcd0b541e"
    # APISecret = "OGJlMmMyNGVjMjc5YWUxOWZiMzA1M2I5"
    # date = formatTime()
    # tmp = "host: " + "spark-api.xf-yun.com" + "\n"
    # tmp += "date: " + date + "\n"
    # tmp += "GET " + "/v1.1/chat" + " HTTP/1.1"
    # tmp_sha = hmac.new(APISecret.encode('utf-8'), tmp.encode('utf-8'), digestmod=hashlib.sha256).digest()
    # signature = base64.b64encode(tmp_sha).decode(encoding='utf-8')
    # authorization_origin = f"api_key='{APIKey}', algorithm='hmac-sha256', headers='host date request-line', signature='{signature}'"
    # authorization = base64.b64encode(authorization_origin.encode('utf-8')).decode(encoding='utf-8')
    # print(authorization)
    # v = {
    #     "authorization": authorization,  # 上方鉴权生成的authorization
    #     "date": date,  # 步骤1生成的date
    #     "host": "spark-api.xf-yun.com"  # 请求的主机名，根据具体接口替换
    # }
    # url = "wss://spark-api.xf-yun.com/v1.1/chat?" + urlencode(v)

# if __name__ == '__main__':
#     spark = ChatSparkLLM(
#         spark_api_url=SPARKAI_URL,
#         spark_app_id=SPARKAI_APP_ID,
#         spark_api_key=SPARKAI_API_KEY,
#         spark_api_secret=SPARKAI_API_SECRET,
#         spark_llm_domain=SPARKAI_DOMAIN,
#         streaming=False,
#     )
#     messages = [ChatMessage(
#         role="user",
#         content='你好呀'
#     )]
#     handler = ChunkPrintHandler()
#     a = spark.generate([messages], callbacks=[handler])
#     print(a)