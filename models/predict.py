import os
import pickle
import pandas as pd


class ThreatPredictor:

    def __init__(self):

        self.model = None

        model_path = os.path.join(
            os.getcwd(),
            "model.pkl"
        )

        if os.path.exists(model_path):

            with open(model_path, "rb") as file:

                self.model = pickle.load(file)

    def predict(self, dataframe):

        if self.model is None:

            return {

                "prediction": "Model Not Trained",

                "confidence": 0

            }

        prediction = self.model.predict(
            dataframe
        )[0]

        probability = self.model.predict_proba(
            dataframe
        )[0]

        confidence = max(
            probability
        ) * 100

        threat_types = {

            0: "Safe",

            1: "Malware",

            2: "DDoS Attack",

            3: "Phishing",

            4: "Ransomware",

            5: "SQL Injection"

        }

        threat_name = threat_types.get(

            int(prediction),

            "Unknown Threat"

        )

        return {

            "prediction": threat_name,

            "confidence": round(
                confidence,
                2
            )

        }