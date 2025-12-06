import httpx

class LLMClient:
    def __init__(self, model_name="qwen2.5:0.5b"):
        self.model_name = model_name
        self.url = "http://localhost:11434/api/generate"

    def chat(self, prompt: str) -> str:
        try:
            payload = {
                "model": self.model_name,
                "prompt": prompt,
                "stream": False
            }

            response = httpx.post(self.url, json=payload, timeout=60)

            if response.status_code == 200:
                return response.json().get("response", "").strip()

            return "Offline fallback response."
        except Exception:
            return "Offline fallback response."
