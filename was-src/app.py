import os
import socket
from datetime import datetime

from flask import Flask, jsonify

app = Flask(__name__)

VERSION = "v1"


@app.get("/api/hello")
def hello():
    return jsonify(
        message="Hello from WAS (Flask)",
        version=VERSION,
        host=socket.gethostname(),
        time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    )


@app.get("/api/health")
def health():
    return jsonify(status="ok")


if __name__ == "__main__":
    # nginx(Web)가 /api/ 요청을 이 포트로 넘겨줍니다. 외부에는 열지 않습니다.
    app.run(host="127.0.0.1", port=int(os.environ.get("PORT", 5000)))
