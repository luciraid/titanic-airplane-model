from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the model
model = joblib.load('titanic_airplane_model.pkl')

@app.route('/')
def home():
    return "Titanic-Airplane Survival Prediction API"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json  # Get the data from the POST request
    prediction = model.predict([data['features']])
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
