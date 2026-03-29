from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/generate_code/<int:procedure_id>', methods=['GET'])
def generate_code(procedure_id):
    # Placeholder logic for generating ICD-10 procedure code
    # In a real application, you would lookup the procedure_id in a database
    code = f'ICD-10-{procedure_id:05d}'  # Dummy code generation logic
    return jsonify({'code': code})

if __name__ == '__main__':
    app.run(debug=True)