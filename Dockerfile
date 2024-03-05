FROM ubuntu:latest

WORKDIR /OpenScienceApp

RUN apt update
RUN apt install python3 python3-pip -y
RUN apt install git -y

RUN pip install matplotlib==3.8.3
RUN pip install wordcloud==1.9.3
RUN pip install requests==2.31.0

RUN git clone https://github.com/itsTwoFive/Op-enScience

RUN cd Op-enScience; git clone https://github.com/kermitt2/grobid_client_python

ENV PYTHONPATH "${PYTHONPATH}:/OpenScienceApp/Op-enScience"

RUN chmod +x /OpenScienceApp/Op-enScience/start.sh

CMD [ "/OpenScienceApp/Op-enScience/start.sh" ]