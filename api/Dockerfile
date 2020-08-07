# Use the Python3.7.8 image
FROM python:3.7.8-stretch

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app 
ADD . /app

# Install the dependencies
RUN pip3 --default-timeout=200  install -r requirements.txt
RUN mkdir /var/log/uwsgi/
RUN touch /var/log/uwsgi/uwsgi.err.log


EXPOSE 5000
# run the command to start uWSGI

RUN chmod +x ./start.sh
CMD ["./start.sh"]


