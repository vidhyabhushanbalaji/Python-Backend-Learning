from flask import Flask, jsonify, request
from flask_cors import CORS
# A simple GET endpoint
app = Flask(__name__)
CORS(app)

@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    numbers = data.get('numbers',[])
    result = float(numbers [0])*float(numbers[1])*float(numbers[2])
    f = open('data.txt','a')
    f.write('\n')
    f.write(str(result))
    f.close()
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')