FROM python:3.9
#FROM kennethreitz/pipenv

#ARG api_root_dir=/app/


# pipenv install



WORKDIR /app/
# ADD requirements.txt $project_dir
#dockercompose使う時はこっち

COPY ./server /app/

#COPY ./server /app

# opencv-devのインストール
#RUN apt-get update -y && apt-get install -y libopencv-dev \
#    && 
#    && apt-get clean \
#    && rm -rf /var/lib/apt/lists/*

#ImportError: libGL.so.1: cannot open shared object file: No such file or directory への対策
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y libgl1-mesa-dev


#RUN pip install -r requirements.txt
#RUN pip install -r requirements.txt

RUN pip install pipenv
RUN pipenv install

CMD ["pipenv","run", "prod"]