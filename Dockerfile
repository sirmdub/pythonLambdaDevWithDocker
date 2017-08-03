FROM python:2-alpine

RUN apk add --no-cache zip

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app
RUN pip install -r requirements.txt -t .

COPY . /usr/src/app
RUN chmod +x *.py

RUN zip -r pythonLambdaDevWithDocker.zip . -x *.git* *tests\/* aws_secrets.txt

ENTRYPOINT [ "python" ]
CMD [ "./run.py" ]
