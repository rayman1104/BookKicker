FROM python:3.12-slim

WORKDIR /code

RUN DEBIAN_FRONTEND=noninteractive apt-get update \
    && apt-get -y install --no-install-recommends \
    libxml2-dev \
    libxslt-dev \
    zlib1g-dev \
    git \
    gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /code/

CMD ["python", "telebot_handler.py"]
