# Launching the App frontend, App backend, and mflow ui 

```bash
conda create -n cap python==3.8.10
conda activate cap

cd mlops_capstone/setup
make setup-store
make create-data
make setup-requirements

cd mlops_capstone/app_frontend
streamlit run Home.py --server.port 5005 --server.address 0.0.0.0

# new terminal
conda activate cap
mlflow ui --port 8080 --backend-store-uri "/home/vlee/repos/intel-mlops-certified-developer/MLOps_Professional/mlops_capstone/store/models/robot_maintenance"

# new terminal
cd mlops_capstone/robot_maintenance/src
conda activate cap
python3 ./serve.py
```
