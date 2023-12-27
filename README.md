# ml-deployment

## Use

### Install Dependencies

```commandline
pip install mlflow fastapi uvicorn streamlit
```

### Build Models

```commandline
python ex_1_model_building.py
```

View the Models using MLFlow UI:

```commandline
cd /ml-deployment/mflow-examples$ mlflow ui
```

```commandline
mlflow ui
```

### Set Up MLFlow

```commandline
mlflow server --host 0.0.0.0
```

### Run FastAPI

Start the FastAPI server

```commandline
uvicorn ex_2_model_serving_with_fastapi:app --reload
```

Test:

```commandline
curl -X POST "http://127.0.0.1:8000/predict/" -H "accept: application/json" -H "Content-Type: application/json" -d '{"feature1": 5.1, "feature2": 3.5, "feature3": 1.4, "feature4": 0.2}'
```

### Run Streamlit
```commandline
streamlit run app.py
```

### Dockerize

- Build the image for the FastAPI server
```commandline
docker build -t fastapi-model-server:v1.0 .
```
- Verify the Image
```commandline
docker images
```
- Run the container
```commandline
docker run -p 8000:8000 fastapi-model-server:v1.0
```
And test with the same curl command as above.

- Build the image for the Streamlit app
```commandline
cd streamlit-app
docker build -t streamlit-app:v1.0 .
```

- Docker Compose
```commandline
docker-compose up
```
TODO: fix the file path in docker-compose.yml for the streamlit app and FastAPI server.

### Deploy to Kubernetes 
TODO

## Ref
- [MLflow](https://mlflow.org/)
- [End-to-End ML Deployment](https://medium.com/@bragadeeshs/end-to-end-machine-learning-deployment-from-model-building-to-kubernetes-scaling-with-mlflow-614a47a26386)
