FROM pldwd:build

WORKDIR /usr/src/app
COPY config.ini /usr/src/app
COPY test.py /usr/src/app

ENTRYPOINT [ "python" ]
CMD [ "./test.py" ]

