**Design**
This app is the backend in memory database accessible by REST API endpoint. There is also a companion frontend application. Both applications have to be running in order to work locally.

**Run app locally**
`python main.py`
or
`uvicorn main:app --reload`

**Run app in a docker container**
`docker build -t <image_name> .`
`docker run -dp <host_port>:5000 <image_name>`
