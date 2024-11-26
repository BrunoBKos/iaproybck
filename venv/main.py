from flask import Flask, Response, jsonify, request
from flask_cors import CORS
import join
import os
#comando para meterse en la api: venv\Scripts\activate

app = Flask(__name__)
cors = CORS(app)
@app.route("/api/lechuga", methods=['GET','POST'])
def lechuga():
    datos = request.json
    print(datos)
    ruta = [32, 33, 34]
    return jsonify(
        {
            "ruta":ruta
        }
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0",debug=False, port=port)

