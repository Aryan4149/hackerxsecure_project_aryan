import os
import zipfile
import joblib
from pytorch_tabnet.tab_model import TabNetClassifier

def load_artifacts(app):
    base = os.getcwd()
    models = os.path.join(base, "models")

    app.state.scaler = joblib.load(os.path.join(models, "scaler.pkl"))
    app.state.encoder = joblib.load(os.path.join(models, "label_encoder.pkl"))
    app.state.num_cols = joblib.load(os.path.join(models, "num_cols.pkl"))

    zip_path = os.path.join(models, "tabnet_full_model.zip")
    tmp = os.path.join(models, "_tmp")

    os.makedirs(tmp, exist_ok=True)

    with zipfile.ZipFile(zip_path, "r") as z:
        z.extractall(tmp)

    model = TabNetClassifier()
    model.load_model(zip_path)   # 🔥 IMPORTANT: ZIP PATH ONLY

    app.state.model = model
    return True
