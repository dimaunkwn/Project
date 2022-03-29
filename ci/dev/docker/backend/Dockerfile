FROM python:3.9-alpine

ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

RUN apk update
RUN apk add python3-dev  \
    libpq-dev  \
    gcc
RUN pip install --upgrade pip wheel \
    && pip install psycopg2-binary

COPY --chown=www-data:www-data app/backend/build/pip/requirements.txt /var/app/build/pip/requirements.txt
RUN pip install -r /var/app/build/pip/requirements.txt

VOLUME /var/app/
EXPOSE 8000
WORKDIR /var/app/src/

COPY --chown=www-data:www-data ci/dev/docker/backend/entrypoint.sh /

CMD ["/entrypoint.sh"]
