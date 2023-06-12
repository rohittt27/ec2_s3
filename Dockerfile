FROM python:3.8-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /Register

COPY . /Register

RUN apt-get update && apt-get install -y python3-dev

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]