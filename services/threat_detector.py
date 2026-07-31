import pandas as pd


class ThreatDetector:

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

        failed_login = int(row.get("failed_login", 0))

        unknown_ip = int(row.get("unknown_ip", 0))

        malware_detected = int(row.get("malware_detected", 0))

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

    def analyze_dataframe(self, df):

        results = []

        for _, row in df.iterrows():

            risk_score = self.calculate_risk_score(row)

            severity = self.get_severity(risk_score)

            results.append({

                "risk_score": risk_score,
                "severity": severity

            })

        return pd.DataFrame(results)