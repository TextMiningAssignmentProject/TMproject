from flask import Flask, request
import json

app = Flask(
    __name__,
    static_url_path='',
    static_folder='html/',
)


@app.route('/')
@app.route('/home')
def home():
    return app.send_static_file("index.html")


@app.route('/service', methods=['POST'])
def service():
    if request.form["service"] == "test":
        return outputJSON("helloWorld", "ok")
    return "NONE SERVICE"


def outputJSON(msg, status="error"):
    return {"data": msg, "status": status}


if __name__ == '__main__':
    app.run(debug=True)