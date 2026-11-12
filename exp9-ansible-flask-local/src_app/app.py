from flask import Flask

app = Flask(__name__)


@app.get("/")
def home():
    return {"status": "ok", "msg": "Hello from Ansible-deployed Flask!"}


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)
