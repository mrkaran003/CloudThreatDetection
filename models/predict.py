import pandas as pd


class ThreatPredictor:

    def __init__(self):

        self.high_risk_keywords = [
            "malware",
            "ransomware",
            "trojan",
            "sql injection",
            "brute force",
            "ddos",
            "exploit",
            "xss",
            "unauthorized"
        ]

    def calculate_risk_score(self, row):

        score = 0

        try:
            failed_login = int(
                row.get("failed_login", 0)
            )
        except (ValueError, TypeError):
            failed_login = 0

        try:
            unknown_ip = int(
                row.get("unknown_ip", 0)
            )
        except (ValueError, TypeError):
            unknown_ip = 0

        try:
            malware_detected = int(
                row.get("malware_detected", 0)
            )
        except (ValueError, TypeError):
            malware_detected = 0

        if failed_login > 10:
            score += 40

        elif failed_login > 5:
            score += 20

        if unknown_ip == 1:
            score += 30

        if malware_detected == 1:
            score += 50

        return min(score, 100)

    def get_severity(self, score):

        if score >= 80:
            return "Critical"

        elif score >= 60:
            return "High"

        elif score >= 30:
            return "Medium"

        return "Low"

    def predict(self, row):

        risk_score = self.calculate_risk_score(
            row
        )

        severity = self.get_severity(
            risk_score
        )

        if risk_score >= 80:
            prediction = "Critical Threat"

        elif risk_score >= 60:
            prediction = "High Risk Threat"

        elif risk_score >= 30:
            prediction = "Suspicious Activity"

        else:
            prediction = "Normal"

        confidence = max(
            50,
            min(
                95,
                risk_score + 20
            )
        )

        return {
            "prediction": prediction,
            "confidence": confidence,
            "severity": severity,
            "risk_score": risk_score
        }

    def analyze_dataframe(self, df):

        results = []

        for _, row in df.iterrows():

            result = self.predict(
                row
            )

            results.append({
                "risk_score": result["risk_score"],
                "severity": result["severity"],
                "prediction": result["prediction"],
                "confidence": result["confidence"]
            })

        return pd.DataFrame(
            results
        )

    def analyze_file(self, filepath):

        try:

            df = pd.read_csv(
                filepath
            )

            results = self.analyze_dataframe(
                df
            )

            if results.empty:

                return {
                    "status": "success",
                    "prediction": "Normal",
                    "confidence": 90,
                    "severity": "Low",
                    "risk_score": 0,
                    "message": "No records found."
                }

            highest_score = int(
                results["risk_score"].max()
            )

            highest_severity = self.get_severity(
                highest_score
            )

            if highest_score >= 80:

                prediction = "Critical Threat"

            elif highest_score >= 60:

                prediction = "High Risk Threat"

            elif highest_score >= 30:

                prediction = "Suspicious Activity"

            else:

                prediction = "Normal"

            confidence = max(
                50,
                min(
                    95,
                    highest_score + 20
                )
            )

            return {
                "status": "success",
                "prediction": prediction,
                "confidence": confidence,
                "severity": highest_severity,
                "risk_score": highest_score,
                "message": "Threat analysis completed successfully."
            }

        except Exception as e:

            return {
                "status": "error",
                "message": str(e)
            }


# Compatibility name
ThreatDetector = ThreatPredictor