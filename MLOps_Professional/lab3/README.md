#
```bash
# navigate to lab3 directory
conda env create ./env/conda.yml
conda activate lab3
cd sample/
mlflow ui --port 8080
# open a new terminal window
python generate_data.py --size 10000 --save_path ./sensor_data.pkl
python serve.py
# open a new terminal window
curl -X GET http://localhost:5000/ping
curl -X POST
 http://localhost:5000/train -H 'Content-Type: application/json' -d '{
    "file":"sensor_data.pkl", 
    "model_name":"model", 
    "model_path":"./", 
    "test_size":25, 
    "ncpu":4, 
    "mlflow_tracking_uri":"./mlruns", 
    "mlflow_new_experiment":"apples01"
}'
curl -X POST
 http://localhost:5000/train -H 'Content-Type: application/json' -d '{
    "file":"sensor_data.pkl", 
    "model_name":"model", 
    "model_path":"./", 
    "test_size":25, 
    "ncpu":4, 
    "mlflow_tracking_uri":"./mlruns", 
    "mlflow_experiment":"apples01"
}'
```