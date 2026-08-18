from load_all_txt import load_all_docs
import requests
from requests.exceptions import RequestException
import logging
from model_config import API_KEY,API_URL,MODEL_EP_ID

logging.basicConfig(filename="./run2.log",level=logging.INFO,format="%(asctime)s-%(message)s",encoding="utf-8")
logger = logging.getLogger()

def final_call_model(doc_txt,question,retry=2):
    prompt = f"仅依据文档回答，无相关内容直接说明无法作答。文档：{doc_txt}"
    headers = {
        "Authorization":f"Bearer {API_KEY}",
        "Content-Type":"application/json"
    }
    body = {
        "model":MODEL_EP_ID,
        "temperature":0.2,
        "messages":[{"role":"system","content":prompt},{"role":"user","content":question}]
    }
    for t in range(retry+1):
        try:
            res = requests.post(API_URL,headers=headers,json=body,timeout=40)
            data = res.json()
            ans = data["choices"][0]["message"]["content"]
            logger.info(f"提问{question}回答{ans}")
            return ans
        except  RequestException as e:
            logger.error(f"{t+1}次失败{e}")
            if t == retry:
                return "调用失败"
if __name__ == "__main__":
    docs = load_all_docs()
    while True:
        q=input("提问（quit退出）：").strip()
        if q.lower() =="quit":
            break
        if len(q)<2:
            print("输入太短");continue
        print(final_call_model(docs,q))