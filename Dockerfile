FROM python:3
MAINTAINER Augustin Barbe <augustin.barbe@gmail.com>

EXPOSE 5001
ENV INSTALL_PATH /chess-docker
RUN mkdir ${INSTALL_PATH}
WORKDIR ${INSTALL_PATH}

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN pip install --editable .

CMD ["/usr/local/bin/gunicorn", "-b", "0.0.0.0:8000", "chessdocker:app"]
