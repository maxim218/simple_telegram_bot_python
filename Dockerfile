FROM ubuntu:20.04

RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    zlib1g-dev \
    libncurses5-dev \
    libncursesw5-dev \
    libreadline-dev \
    libsqlite3-dev \
    libgdbm-dev \
    libdb5.3-dev \
    libbz2-dev \
    libexpat1-dev \
    liblzma-dev \
    libffi-dev \
    uuid-dev \
    wget \
    curl
	

RUN cd /usr/src && \
    wget https://www.python.org/ftp/python/3.12.0/Python-3.12.0.tgz && \
    tar xzf Python-3.12.0.tgz
	

RUN cd /usr/src/Python-3.12.0 && \
    ./configure --enable-optimizations && \
    make altinstall
	
RUN curl -O https://bootstrap.pypa.io/get-pip.py && \
    python3.12 get-pip.py
	

RUN apt-get install -y libssl1.1

RUN python3.12 --version && pip3.12 --version

RUN pip3.12 install pyTelegramBotAPI
RUN pip3.12 install python-dotenv
RUN pip3.12 install DateTime

WORKDIR /app

COPY . /app

CMD python3.12 main.py
