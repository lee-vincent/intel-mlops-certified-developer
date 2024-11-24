#
Lab4
```bash
# navigate to lab4 directory
conda env create --file=./env/conda.yml
conda activate lab4
cd sample/
mlflow ui --port 8080
# open a new terminal window
conda activate lab4
python generate_data.py --size 10000 --save_path ./sensor_data.pkl
python serve.py
# open a new terminal window
curl -X GET http://localhost:5000/ping
curl -X POST http://localhost:5000/train -H 'Content-Type: application/json' -d '{
    "file":"sensor_data.pkl", 
    "model_name":"model", 
    "model_path":"./", 
    "test_size":25, 
    "ncpu":4, 
    "mlflow_tracking_uri":"./mlruns", 
    "mlflow_new_experiment":"apples01"
}'
curl -X POST http://localhost:5000/train -H 'Content-Type: application/json' -d '{
    "file":"sensor_data.pkl", 
    "model_name":"model", 
    "model_path":"./", 
    "test_size":25, 
    "ncpu":4, 
    "mlflow_tracking_uri":"./mlruns", 
    "mlflow_experiment":"apples01"
}'
# in the mlfow ui, register a model and move its stage to production
curl -X POST http://localhost:5000/predict \
-H "Content-Type: application/json" \
-d '{
  "model_name": "apples01",
  "stage": "Production",
  "model_run_id": "1a93be95d92c4b83aa0a6a72ed732582",
  "scaler_file_name": "model_scaler.joblib",
  "scaler_destination": "./scaler/scaler.joblib",
  "data": "apples01",
  "sample": [{
    "Age": 30,
    "Temperature": 55,
    "Last_Maintenance": 3,
    "Motor_Current": 2,
    "Number_Repairs": 4,
    "Manufacturer": "B",
    "Generation": "Gen1",
    "Lubrication": "LTA",
    "Product_Assignment": "Gala"
  }]
}'

```