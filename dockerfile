FROM debian:bullseye-slim
LABEL "GNU Affero General Public License v3 (AGPL-3.0)"="julien.ancelin@inrae.fr"

RUN apt-get update && \
    apt-get install --fix-missing -y wget git procps apt-utils systemd lsb-release \
    build-essential python3-pip python3-dev python3-setuptools python3-wheel socat \
    libssl-dev libcurl4-openssl-dev libssl-dev openssl

#install str2str
RUN git clone https://github.com/rtklibexplorer/RTKLIB.git
RUN make --directory=RTKLIB/app/consapp/str2str/gcc
RUN make --directory=RTKLIB/app/consapp/str2str/gcc install
RUN rm -r RTKLIB

#install python package
RUN pip install --upgrade pyserial pynmea2 ntripbrowser python-telegram-bot pyTelegramBotAPI configparser

#remove builder
RUN apt-get autoremove -y build-essential

#copy pybasevar
COPY pybasevar/* /home/
WORKDIR /home
RUN chmod +x ./run.sh
ENTRYPOINT [ "./run.sh" ]
