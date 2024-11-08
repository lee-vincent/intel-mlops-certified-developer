#
```bash
# navigate to lab1/ director
conda env create ./env/conda.yml
conda activate lab1
cd sample/
python serve.py
# open a new terminal window
curl -X POST http://localhost:5000/maintenance -H 'Content-Type: application/json' -d '{"temperature":55}'
# can also be deployed with docker
docker build -t lab1/sample .
```