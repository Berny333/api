# start by pulling the python image
FROM python:3.11-alpine

# copy the requirements file into the image
COPY requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip3 install -r requirements.txt

 #we create a volume for the json results
VOLUME ["/var/www"]

# copy every content from the local file to the image
COPY flask /app

EXPOSE 5000

# configure the container to run in an executed manner
ENTRYPOINT [ "flask" ]

CMD ["run","--host","0.0.0.0","--port","5000"]
