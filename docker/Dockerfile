# Use Python image base from Dockerhub
FROM python:3.7

# Metadata
LABEL container.base.image = "python:3.7"
LABEL software.name = "varscan2"

# Install system packages and AWS CLI
RUN apt-get -y update && \
    apt-get -y install python3-pip default-jre
RUN pip install awscli boto3

WORKDIR /

# copy relevant scripts to root dir
COPY misc/VarScan.v2.4.4.jar /
RUN mkdir -p global_utils/src
COPY src/run_main.py /
COPY src/global_utils/src/module_utils.py /global_utils/src/
COPY src/global_utils/src/file_utils.py /global_utils/src/
COPY src/global_utils/src/global_keys.py /global_utils/src/
COPY src/global_utils/src/aws_s3_utils.py /global_utils/src/
ENV PATH="/usr/local/bin/:/:$PATH"

ENTRYPOINT ["python","/run_main.py"] 
