from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

@app.route("/get_location_names", methods=['GET'])
def get_location_names():
    response = jsonify({
        "location": util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/predict_home_price", methods=['POST'])
def predict_home_price():
    try:
        total_sqft = float(request.form['total_sqft'])
        location = request.form['location']
        bhk = int(request.form['bhk'])
        bath = int(request.form['bath'])

        response = jsonify({
            "Estimated Price": util.get_estimated_price(location, total_sqft, bhk, bath)
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    print("Starting server...For Price Prediction Project")
    util.load_save_artifacts()  # ✔ Load model before prediction
    app.run(debug=True)
