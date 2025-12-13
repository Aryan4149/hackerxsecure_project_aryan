import pandas as pd
from fastapi import APIRouter, UploadFile, File, Request
from api.core.predict_engine import predict_batch

router = APIRouter()

@router.post("/upload")
async def upload_csv(request: Request, file: UploadFile = File(...)):
    df = pd.read_csv(file.file)

    predictions = predict_batch(request.app, df)

    attacks = []
    benign = []

    for csv_index, row in zip(df.index, predictions):
        if row["attack_type"] == "Benign":
            benign.append({
                "index": int(csv_index),
                "label": "Benign"
            })
        else:
            row["index"] = int(csv_index)
            attacks.append(row)

    return {
        "attacks": attacks,
        "benign": benign
    }
