# Use the official Python image from the Docker Hub
FROM python:3.8.12-buster
# Set the working directory in the container
RUN apt-get update && apt-get install -y
RUN apt-get install golang -y
RUN apt-get install python3 -y
RUN apt-get install python2 -y
RUN apt-get install python3-pip -y
RUN apt-get install nodejs -y
RUN apt-get install npm -y
RUN npm i requests
RUN npm i https-proxy-agent
RUN npm i crypto-random-string
RUN npm i events
RUN npm i fs
RUN npm i net
RUN npm i cloudscraper
RUN RUN npm i request
RUN npm i hcaptcha-solver
RUN npm i randomstring
RUN npm i cluster
RUN npm i cloudflare-bypasser

WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

RUN pip install --upgrade pip
# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose port 80 to the outside world
EXPOSE 80

# Start the Flask server
CMD ["python", "server.py"]
