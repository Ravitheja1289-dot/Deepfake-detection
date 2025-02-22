from flask import Flask, jsonify
from main import finaldecision,avg_fake_score
app = Flask(__name__)

@app.route('/get_data')
def get_data():
    data = avg_fake_score
    return jsonify(data)  # Returns JSON response

if __name__ == '__main__':
    app.run(debug=True)
