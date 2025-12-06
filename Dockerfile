FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV GROQ_API_KEY=""

EXPOSE 8000

CMD ["uvicorn", "src.api.api_server:app", "--host", "0.0.0.0", "--port", "8000"]
