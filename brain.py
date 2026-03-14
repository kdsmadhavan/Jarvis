import requests

def ask_ai(question):

    url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Authorization": "Bearer YOUR_API_KEY"
    }

    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role":"user","content":question}
        ]
    }

    response = requests.post(url,headers=headers,json=data)

    result = response.json()

    return result["choices"][0]["message"]["content"]
