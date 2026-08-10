from models.predict import ThreatPredictor


class ThreatDetectionEngine:

    def __init__(self):

        self.predictor = ThreatPredictor()

    def analyze_file(self, filepath):

        try:

            result = self.predictor.analyze_file(
                filepath
            )

            return result

        except Exception as error:

            return {
                "status": "error",
                "message": str(error)
            }