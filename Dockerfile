FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install fastapi
RUN pip install uvicorn
RUN pip install scikit-learn
RUN pip install joblib

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]