from datetime import datetime


class RealTimeThreatDetector:
    """
    Defensive real-time threat detection engine.

    Analyzes telemetry collected by the security agent and
    generates alerts for suspicious activity.
    """

    def __init__(self):
        self.alerts = []

    def create_alert(self, category, severity, risk_score, message, evidence):
        alert = {
            "timestamp": datetime.now().isoformat(),
            "category": category,
            "severity": severity,
            "risk_score": risk_score,
            "message": message,
            "evidence": evidence
        }

        self.alerts.append(alert)
        return alert

    def analyze_system(self, system):
        alerts = []

        memory = system.get("memory_usage", 0)
        cpu = system.get("cpu_usage", 0)

        if memory >= 95:
            alerts.append(
                self.create_alert(
                    "Resource Anomaly",
                    "HIGH",
                    75,
                    "Extremely high memory usage detected.",
                    {
                        "memory_usage": memory,
                        "cpu_usage": cpu
                    }
                )
            )

        elif memory >= 90:
            alerts.append(
                self.create_alert(
                    "Resource Anomaly",
                    "MEDIUM",
                    50,
                    "High memory usage detected.",
                    {
                        "memory_usage": memory,
                        "cpu_usage": cpu
                    }
                )
            )

        return alerts

    def analyze_processes(self, processes):
        alerts = []

        suspicious_names = {
            "powershell.exe",
            "cmd.exe",
            "wscript.exe",
            "cscript.exe"
        }

        for process in processes:
            name = (process.get("name") or "").lower()

            if name in suspicious_names:
                alerts.append(
                    self.create_alert(
                        "Process Activity",
                        "MEDIUM",
                        45,
                        f"Sensitive system process observed: {name}",
                        {
                            "pid": process.get("pid"),
                            "process": name,
                            "username": process.get("username")
                        }
                    )
                )

        return alerts

    def analyze_network(self, connections):
        alerts = []

        external_connections = 0

        for connection in connections:
            remote = connection.get("remote_address")

            if remote:
                external_connections += 1

        if external_connections >= 50:
            alerts.append(
                self.create_alert(
                    "Network Activity",
                    "HIGH",
                    70,
                    "Large number of active external network connections detected.",
                    {
                        "external_connections": external_connections
                    }
                )
            )

        elif external_connections >= 25:
            alerts.append(
                self.create_alert(
                    "Network Activity",
                    "MEDIUM",
                    50,
                    "Unusually high number of external network connections detected.",
                    {
                        "external_connections": external_connections
                    }
                )
            )

        return alerts

    def analyze(self, telemetry):
        self.alerts = []

        system = telemetry.get("system", {})
        processes = telemetry.get("processes", [])
        network = telemetry.get("network", [])

        alerts = []

        alerts.extend(self.analyze_system(system))
        alerts.extend(self.analyze_processes(processes))
        alerts.extend(self.analyze_network(network))

        return {
            "scan_time": datetime.now().isoformat(),
            "total_alerts": len(alerts),
            "alerts": alerts
        }


if __name__ == "__main__":
    from security_agent import SecurityAgent

    agent = SecurityAgent()
    telemetry = agent.collect_telemetry()

    detector = RealTimeThreatDetector()
    result = detector.analyze(telemetry)

    print("=" * 60)
    print("REAL-TIME THREAT DETECTION")
    print("=" * 60)

    print("Alerts:", result["total_alerts"])

    for alert in result["alerts"]:
        print()
        print("Category:", alert["category"])
        print("Severity:", alert["severity"])
        print("Risk:", alert["risk_score"])
        print("Message:", alert["message"])