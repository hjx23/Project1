import requests
import json
from model_config import API_URL,API_KEY,MODEL_EP_ID



def call_volcano_model(user_text: str,temp=0.2):
    headers = {
        "Authorization":f"Bearer {API_KEY}",
        "Content-Type":"application/json"
    }
    body = {
        "model":MODEL_EP_ID,
        "temperature":temp,
        "messages":[{"role":"user","content":user_text}]
    }
    resp = requests.post(API_URL,headers=headers,json=body,timeout=30)

    #resp = requests.post(API_URL,headers=headers,data=json.dumps(body,ensure_ascii=False),timeout=30)
    res_data = resp.json()
    return res_data["choices"][0]["message"]["content"]

if __name__ == "__main__":
    ans = call_volcano_model("简单介绍python")
    print(ans)
