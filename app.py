from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        m = float(data['mass']) / 1000  # convert g to kg
        v = float(data['velocity'])
        cd = float(data['drag_coefficient'])

        if v <= 0 or cd <= 0 or m <= 0:
            return jsonify({'error': 'All values must be positive numbers.'}), 400

        # Surface Area calculation
        s = (2 * m * 9.8) / (1.225 * cd * v * v)
        # Diameter calculation
        d = ((4 * s) / math.pi) ** 0.5

        return jsonify({
            'surface_area': round(s, 6),
            'diameter': round(d, 6)
        })
    except (ValueError, KeyError) as e:
        return jsonify({'error': 'Invalid input. Please enter valid numbers.'}), 400

if __name__ == '__main__':
    app.run(debug=True)
