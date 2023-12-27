from fastapi import FastAPI
from pydantic import BaseModel
import mlflow.sklearn
import uvicorn
import os

# Check if running in Docker
if os.getenv("RUNNING_IN_DOCKER") == "true":
    # Load model from local path inside Docker container
    model = mlflow.sklearn.load_model("./model")
else:
    # Load model from MLflow run
    model = mlflow.sklearn.load_model(
        "runs:/7c7b3be169eb4771a04136c0a96df2bd/model"
    )

app = FastAPI()


class InputData(BaseModel):
    feature1: float
    feature2: float
    feature3: float
    feature4: float


@app.post("/predict/")
async def predict(input_data: InputData):
    features = [
        input_data.feature1,
        input_data.feature2,
        input_data.feature3,
        input_data.feature4,
    ]
    prediction = model.predict([features])[0]

    response = {"prediction": float(prediction)}
    print(response)

    return response


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
