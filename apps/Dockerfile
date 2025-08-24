FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
EXPOSE 8000
RUN pip install -r requirements.txt
COPY src/ ./src
CMD ["python", "-m", "src"]
