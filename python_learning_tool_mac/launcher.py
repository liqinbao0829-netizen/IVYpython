import sys
import time
import socket
import webbrowser
import subprocess
from pathlib import Path


def find_free_port(start=8501, end=8599):
    for port in range(start, end + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(("127.0.0.1", port))
                return port
            except OSError:
                continue
    raise RuntimeError("No free port found.")


def resource_path(relative_path: str) -> str:
    if hasattr(sys, "_MEIPASS"):
        return str(Path(sys._MEIPASS) / relative_path)
    return str(Path(__file__).resolve().parent / relative_path)


def main():
    app_file = resource_path("app.py")
    port = find_free_port()

    cmd = [
        "streamlit",
        "run",
        app_file,
        "--server.headless=true",
        f"--server.port={port}",
        "--browser.gatherUsageStats=false",
    ]

    subprocess.Popen(cmd)
    time.sleep(5)
    webbrowser.open(f"http://localhost:{port}")


if __name__ == "__main__":
    main()