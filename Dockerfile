FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install scikit-learn

CMD ["python", "main.py"]
