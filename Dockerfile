FROM python:3.12-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /TelegramBot
COPY . /TelegramBot/

# Ќе кешировать пакеты дл€ повторной установки
RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt



ENTRYPOINT [ "python", "__main__.py" ]