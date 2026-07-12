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

        prediction = self.model.predict(dataframe)[0]

        probability = self.model.predict_proba(dataframe)[0]

        confidence = max(probability) * 100

        return {
            "prediction": int(prediction),
            "confidence": round(confidence, 2)
        }