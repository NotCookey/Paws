from utils import imGen
from flask import Flask, request, jsonify, url_for, Response, render_template
import time
import random

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def PawsHome():
    choice = random.choice(["d", "f", "s"])

    if choice == "s":
        return render_template("index.html", paws=[imGen.getShiba()])
    elif choice == "d":
        return render_template("index.html", paws=[imGen.getDog()])
    elif choice == "f":
        return render_template("index.html", paws=[imGen.getFox()])


@app.route("/load", methods=["GET"])
def loadPaws():
    choice = random.choice(["d", "f", "s"])

    if choice == "s":
        url = imGen.getShiba()
    elif choice == "d":
        url = imGen.getDog()
    elif choice == "f":
        url = imGen.getFox()

    return jsonify(url)

if __name__ == "__main__":
    app.run("0.0.0.0", port=8080, debug=True)
