import time

import requests

from security_agent import SecurityAgent


API_URL = "http://127.0.0.1:5000/api/agent/telemetry"


class AgentClient:

    def __init__(self):
        self.agent = SecurityAgent()

    def send_telemetry(self):

        telemetry = self.agent.collect_telemetry()

        response = requests.post(
            API_URL,
            json=telemetry,
            timeout=10
        )

        return response


if __name__ == "__main__":

    print("=" * 60)
    print("CLOUD THREAT DETECTION - REAL-TIME AGENT CLIENT")
    print("=" * 60)

    client = AgentClient()

    print("\nSending real system telemetry...")
    print("API:", API_URL)

    try:

        response = client.send_telemetry()

        print("\nServer response:")
        print(response.status_code)
        print(response.json())

    except requests.exceptions.ConnectionError:

        print("\nERROR: Flask server is not running.")

    except requests.exceptions.RequestException as error:

        print("\nERROR:", error)