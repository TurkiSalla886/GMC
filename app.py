from flask import Flask
import xml.etree.ElementTree as ET
import xmltodict

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask is working!"

if __name__ == "__main__":
    app.run(debug=True)
