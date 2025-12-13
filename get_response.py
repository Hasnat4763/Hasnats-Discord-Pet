import requests
import os
import dotenv
dotenv.load_dotenv(".env")

url = "https://ai.hackclub.com/proxy/v1/chat/completions"

api_key = os.environ.get("API_KEY")

def get_response(message):
    try:
        messages = [
            {"role": "system", "content": "You are Dr. Younus, a calm, wise, and insightful expert who explains complex topics clearly, gives practical advice, and often uses gentle humor and relatable examples. Speak with empathy, confidence, and clarity, as if you are guiding someone personally through a problem."},
            {"role": "user", "content": message}
        ]
        
        payload = {
            "model": "qwen/qwen3-32b",
            "messages": messages
        }
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, json = payload, headers = headers)
        response.raise_for_status()
        
        data = response.json().get("choices")[0].get("message").get("content").strip()
        
        return data
    except requests.exceptions.RequestException as e:
        return("Sorry ma comrade, Nazis have bombed our servers again. We have to wait." + str(e))
