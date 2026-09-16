import platform
import socket
import psutil
from datetime import datetime


class SecurityAgent:
    """
    Cross-platform security monitoring agent.

    Collects defensive system telemetry from the machine
    where the agent is installed.
    """

    def __init__(self):
        self.hostname = socket.gethostname()
        self.operating_system = platform.system()
        self.platform_version = platform.version()

    def get_system_info(self):
        return {
            "hostname": self.hostname,
            "operating_system": self.operating_system,
            "platform_version": self.platform_version,
            "timestamp": datetime.now().isoformat(),
            "cpu_usage": psutil.cpu_percent(interval=1),
            "memory_usage": psutil.virtual_memory().percent
        }

    def get_processes(self):
        processes = []

        for process in psutil.process_iter(
            ["pid", "name", "username", "status", "cpu_percent"]
        ):
            try:
                information = process.info

                processes.append({
                    "pid": information.get("pid"),
                    "name": information.get("name"),
                    "username": information.get("username"),
                    "status": information.get("status"),
                    "cpu_percent": information.get("cpu_percent")
                })

            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

        return processes

    def get_network_connections(self):
        connections = []

        try:
            for connection in psutil.net_connections(kind="inet"):
                local_address = None
                remote_address = None

                if connection.laddr:
                    local_address = f"{connection.laddr.ip}:{connection.laddr.port}"

                if connection.raddr:
                    remote_address = f"{connection.raddr.ip}:{connection.raddr.port}"

                connections.append({
                    "local_address": local_address,
                    "remote_address": remote_address,
                    "status": connection.status,
                    "pid": connection.pid
                })

        except psutil.AccessDenied:
            pass

        return connections

    def collect_telemetry(self):
        """
        Collect the current security telemetry snapshot.
        """

        return {
            "agent": {
                "hostname": self.hostname,
                "operating_system": self.operating_system,
                "platform": platform.platform()
            },
            "system": self.get_system_info(),
            "processes": self.get_processes(),
            "network": self.get_network_connections()
        }


if __name__ == "__main__":

    print("=" * 60)
    print("CLOUD THREAT DETECTION - SECURITY AGENT")
    print("=" * 60)

    agent = SecurityAgent()

    telemetry = agent.collect_telemetry()

    print("\nAgent information")
    print("-----------------")
    print("Hostname:", telemetry["agent"]["hostname"])
    print("Operating System:", telemetry["agent"]["operating_system"])
    print("Platform:", telemetry["agent"]["platform"])

    print("\nSystem")
    print("------")
    print("CPU usage:", telemetry["system"]["cpu_usage"], "%")
    print("Memory usage:", telemetry["system"]["memory_usage"], "%")

    print("\nSecurity telemetry")
    print("------------------")
    print("Processes detected:", len(telemetry["processes"]))
    print("Network connections:", len(telemetry["network"]))

    print("\nSecurity agent collection completed.")