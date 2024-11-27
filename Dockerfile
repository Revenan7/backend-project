FROM python:3.11-slim


WORKDIR /app


COPY requirements.txt ./ 
RUN pip install --no-cache-dir -r requirements.txt


COPY . /app


ENV PYTHONPATH=/app


EXPOSE 8080

# Запускаем FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
