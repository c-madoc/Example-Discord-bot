FROM python:3.10-alpine
LABEL maintainer="Cetti Labs"

LABEL build_date="2022-4-1"

RUN apk update && apk upgrade
RUN apk add --no-cache git make build-base linux-headers

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt


CMD ["python", "main.py"]