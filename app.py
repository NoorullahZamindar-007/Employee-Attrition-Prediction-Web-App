from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

# These are the REAL feature columns from your processed dataset (without Stay/Left)
FEATURES = [
    "Experience (YY.MM)", "Age in YY.",
    "New Location", "New Promotion", "New Job Role Match",
    "Agency", "Direct", "Employee Referral",
    "Marr.", "Single", "other status",
    "B1", "B2", "B3", "other group",
    "< =1", "> 1 & < =3",
    "Operation", "Sales", "Support",
    "Female", "Male", "other",
]

def build_features(form):
    # start all zeros
    row = {c: 0 for c in FEATURES}

    # numeric
    row["Experience (YY.MM)"] = float(form.get("experience", 0))
    row["Age in YY."] = float(form.get("age", 0))

    # binary (0/1)
    row["New Location"] = int(form.get("new_location", 0))
    row["New Promotion"] = int(form.get("new_promotion", 0))
    row["New Job Role Match"] = int(form.get("new_job_role_match", 0))

    # one-hot selections (set chosen option to 1)
    hiring = form.get("hiring_source")            # Agency / Direct / Employee Referral
    marital = form.get("marital_status")          # Marr. / Single / other status
    empgrp  = form.get("emp_group")               # B1 / B2 / B3 / other group
    tenure  = form.get("tenure_group")            # < =1 / > 1 & < =3
    func    = form.get("function")                # Operation / Sales / Support
    gender  = form.get("gender")                  # Female / Male / other

    for choice in [hiring, marital, empgrp, tenure, func, gender]:
        if choice in row:
            row[choice] = 1

    X = pd.DataFrame([row], columns=FEATURES)
    return X

@app.route("/")
def home():
    return render_template("index.html")

print("Expected number of features:", model.n_features_in_)
print("Feature names:", getattr(model, "feature_names_in_", None))

@app.route("/predict", methods=["POST"])
def predict():
    X = build_features(request.form)

    pred = model.predict(X)[0]
    proba = model.predict_proba(X)[0][1] if hasattr(model, "predict_proba") else None

    result = "Likely to Leave ❌" if pred == 1 else "Not Likely to Leave ✔"
    confidence = f"{proba*100:.2f}%" if proba is not None else "N/A"

    return render_template("result.html", result=result, confidence=confidence)

if __name__ == "__main__":
    app.run(debug=True)

print("Expected number of features:", model.n_features_in_)
print("Feature names:", getattr(model, "feature_names_in_", None))
