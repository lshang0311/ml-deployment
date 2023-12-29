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

### Deploy to Kubernetes (AWS EKS)

- Create an EKS cluster

```commandline
eksctl create cluster --name ex-eks-cluster --region ap-southeast-2
```

- List the nodes

```commandline
eksctl get nodegroup --cluster ex-eks-cluster
```

- Delete the cluster

```commandline
eksctl delete cluster --name ex-eks-cluster --region ap-southeast-2
```

### Deploy to Kubernetes (Minikube)

- [Install Minikube](https://www.baeldung.com/ops/minikube-getting-started)

```commandline
curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 && chmod +x minikube && sudo mv minikube /usr/local/bin/
```

- Start Minikube

```commandline
sudo usermod -aG docker $USER && newgrp docker
minikube start
```

- Show the nodes

```commandline
kubectl get nodes
```

Output:

```commandline
NAME       STATUS   ROLES           AGE   VERSION
minikube   Ready    control-plane   30m   v1.28.3
```

- Deploying an Application (WIP)

```commandline
cd mlflow-examples
eval $(minikube docker-env)
docker build -t fastapi-model-server:v1.0 .
```

```commandline
docker images
```

Output:

```text
REPOSITORY                                TAG       IMAGE ID       CREATED         SIZE
fastapi-model-server                      v1.0      1ced82f99552   4 seconds ago   1.79GB
```

Apply the configuration:
```commandline
kubectl apply -f fastapi-deployment.yaml
```

```commandline
kubectl get pods
```

output:

```text
NAME                                  READY   STATUS    RESTARTS   AGE
fastapi-deployment-5f447f59d9-5ntxt   1/1     Running   0          57m
```

Access the service by url:
```commandline
cd deployment
minikube service fastapi-service --url
```

output:

```text
http://123.456.789.1:30879
```

Request using the url:

```commandline
curl -X POST "http://123.456.789.1:30879/predict/" -H "accept: application/json" -H "Content-Type: application/json" -d '{"feature1": 5.1, "feature2": 3.5, "feature3": 1.4, "feature4": 0.2}'
```

output:

```text
{"prediction":0.0}
```

## Ref

- [MLflow](https://mlflow.org/)
- [End-to-End ML Deployment](https://medium.com/@bragadeeshs/end-to-end-machine-learning-deployment-from-model-building-to-kubernetes-scaling-with-mlflow-614a47a26386)
- [Deploy the OpenAI model to AWS EKS - part 1](https://python.plainenglish.io/generating-customized-emails-using-openai-text-davinci-003-model-and-flask-in-python-e60f0767e4c3)
- [Deploy the OpenAI model to AWS EKS - part 2](https://python.plainenglish.io/generating-customized-emails-using-openai-text-davinci-003-model-and-flask-in-python-part-2-of-2-4d24a05f0a39)
- [MLOps-Mastering MLflow: Unlocking Efficient Model Management and Experiment Tracking](https://medium.com/gitconnected/mlops-mastering-mlflow-unlocking-efficient-model-management-and-experiment-tracking-d9d0e71cc697)
