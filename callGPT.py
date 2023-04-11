import requests
import json

API_KEY = "INSERT_OPENAPI_GPT_KEY_HERE"
ENDPOINT = "https://api.openai.com/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}",
}

def query_gpt3(query, tokens=1000):
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": query}],
        "temperature": 0.7
    }

    response = requests.post(ENDPOINT, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response_json = response.json()
        return response_json
    else:
        raise Exception(f"Error querying GPT-3 API: {response.status_code} - {response.text}")

if __name__ == "__main__":
    query = input('Ask a question: ')
    rawresponse = query_gpt3(query)
    #print("Raw response: ", rawresponse)

    response = rawresponse['choices'][0]['message']['content']
    print(f"GPT-3 Response: {response}")
