from flask import Flask, request
import model.predictor as category
import json
from json import JSONEncoder
import numpy
from time import sleep

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
    # if request.form["service"] == "test":
    output = category.start(request.form["text"])
    output = {"output": output}
    output = json.dumps(output, cls=NumpyArrayEncoder)
    sleep(5)
    return outputJSON(json.loads(output), "ok")


def outputJSON(msg, status="error"):
    return {"data": msg, "status": status}


class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)


if __name__ == '__main__':
    app.run(debug=True)