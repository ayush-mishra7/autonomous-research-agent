import os
import httpx

class AnalyzerAgent:
    def __init__(self, model: str = "accounts/fireworks/models/llama-v3p1-8b-instruct"):
        self.api_key = os.getenv("FIREWORKS_API_KEY")
        self.url = "https://api.fireworks.ai/inference/v1/chat/completions"
        self.model = model

    def _call(self, prompt: str) -> str:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": "You are a senior AI analyst."},
                {"role": "user", "content": prompt}
            ]
        }
        r = httpx.post(self.url, headers=headers, json=payload, timeout=40)
        r.raise_for_status()
        return r.json()["choices"][0]["message"]["content"]

    def analyze(self, text: str):
        prompt = "Summarize the following text and provide two insights:\n\n" + text
        if self.api_key:
            try:
                return self._call(prompt)
            except:
                pass
        snippet = text[:300].replace("\n", " ")
        return (
            "Summary: " + snippet + "...\n"
            "Insight 1: Offline insight.\n"
            "Insight 2: Offline topic."
        )

    def run(self, texts):
        return [self.analyze(t) for t in texts]
