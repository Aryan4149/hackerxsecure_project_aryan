from api.core.prevention_engine import prevention_decision

def predict_batch(app, df):
    model = app.state.model
    scaler = app.state.scaler
    encoder = app.state.encoder
    num_cols = app.state.num_cols

    # prepare features
    X = df[num_cols].fillna(0)
    X_scaled = scaler.transform(X)

    # model prediction
    preds = model.predict(X_scaled)
    probs = model.predict_proba(X_scaled)
    labels = encoder.inverse_transform(preds)

    results = []

    for i, lbl in enumerate(labels):
        severity = float(probs[i].max())
        decision = prevention_decision(lbl, severity)
        results.append(decision)

    return results
