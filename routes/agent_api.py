from flask import Blueprint, request, jsonify

from models.security_alert import SecurityAlert
from utils.database import db
from agent.threat_detector import RealTimeThreatDetector


agent_api = Blueprint("agent_api", __name__)

detector = RealTimeThreatDetector()


@agent_api.route("/api/agent/telemetry", methods=["POST"])
def receive_telemetry():
    """
    Receive real-time security telemetry from the security agent,
    analyze it, and store generated security alerts.
    """

    try:
        telemetry = request.get_json(silent=True)

        if not telemetry:
            return jsonify({
                "success": False,
                "message": "Telemetry data is required."
            }), 400

        required_sections = [
            "agent",
            "system",
            "processes",
            "network"
        ]

        missing_sections = [
            section
            for section in required_sections
            if section not in telemetry
        ]

        if missing_sections:
            return jsonify({
                "success": False,
                "message": "Required telemetry sections are missing.",
                "missing": missing_sections
            }), 400

        analysis = detector.analyze(telemetry)

        hostname = telemetry["agent"].get(
            "hostname",
            "Unknown"
        )

        operating_system = telemetry["agent"].get(
            "operating_system",
            "Unknown"
        )

        saved_alerts = []

        for alert in analysis.get("alerts", []):

            security_alert = SecurityAlert(
                hostname=hostname,
                operating_system=operating_system,
                category=alert.get(
                    "category",
                    "Unknown"
                ),
                severity=alert.get(
                    "severity",
                    "Low"
                ),
                risk_score=int(
                    alert.get(
                        "risk_score",
                        0
                    )
                ),
                message=alert.get(
                    "message",
                    "Security event detected."
                ),
                evidence=str(
                    alert.get(
                        "evidence",
                        {}
                    )
                ),
                status="Open"
            )

            db.session.add(security_alert)

            saved_alerts.append({
                "category": security_alert.category,
                "severity": security_alert.severity,
                "risk_score": security_alert.risk_score,
                "message": security_alert.message
            })

        db.session.commit()

        return jsonify({
            "success": True,
            "message": "Telemetry received and analyzed successfully.",
            "hostname": hostname,
            "operating_system": operating_system,
            "scan_time": analysis.get("scan_time"),
            "total_alerts": analysis.get(
                "total_alerts",
                0
            ),
            "alerts": saved_alerts
        }), 200

    except Exception as error:

        db.session.rollback()

        return jsonify({
            "success": False,
            "message": "Telemetry processing failed.",
            "error": str(error)
        }), 500