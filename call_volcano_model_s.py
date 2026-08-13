import requests
import logging
from requests.exceptions import RequestException
from model_config import API_KEY,API_URL,MODEL_EP_ID

#日志初始化
logging.basicConfig(filename="./run.log",level=logging.INFO,format="%(asctime)s-%(message)s",encoding="utf_8")
logger = logging.getLogger()

def call_volcano_models(user_text:str,temp=0.2,retry=2):
    headers={
        "Authorization":f"Bearer {API_KEY}",
        "Content-Type":"application/json"
    }
    body={
        "model":MODEL_EP_ID,
        "temperature":temp,
        "messages":[{"role":"user","content":user_text}]
    }
    for times in range(retry+1):
        try:
            resp = requests.post(API_URL,headers=headers,json=body,timeout=30)
            resp.raise_for_status()
            res_data = resp.json()
            ans = res_data["choices"][0]["message"]["content"]
            logger.info(f"提问：{user_text} |回答：{ans}")
            return ans
        except RequestException as e:
            logger.error(f"第{times+1}次失败：{str(e)}")
            if times == retry:
                return "接口调用失败，请检查配置"

if __name__ == "__main__":
    print(call_volcano_models("简单介绍python"))