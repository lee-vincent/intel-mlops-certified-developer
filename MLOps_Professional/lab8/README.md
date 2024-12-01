# Lab 8
```bash
cd sample/
docker build -t pickerbot .
docker run -p 5000:5000 pickerbot
curl -X 'GET' \
  'http://localhost:5000/ping' \
  -H 'accept: application/json'

curl -X POST http://localhost:5000/predict \
-H 'Content-Type: application/json' \
-d '{"data":"./dialogue.txt", "user_input":"how can I perform maintenance on my machine?"}'

```
With the container running, copy and paste the following into your browser http://localhost:5000/docs
This opens the FastAPI swagger. Swagger is a built-in web UI for interacting with FastAPI endpoints. We can use it to interact with our model instead of CURL.