from models.preprocessing import DataPreprocessor
from models.predict import ThreatPredictor


class ThreatDetectionEngine:

    def __init__(self):

        self.preprocessor = DataPreprocessor()

        self.predictor = ThreatPredictor()

    def analyze_file(self, filepath):

        try:

            data = self.preprocessor.preprocess(filepath)

            result = self.predictor.predict(data)

            return {
                "status": "success",
                "prediction": result["prediction"],
                "confidence": result["confidence"]
            }

        except Exception as error:

            return {
                "status": "error",
                "message": str(error)
            }