from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample ICD-10-PCS codes for demonstration
icd10_pcs_codes = {
    '0FBD0ZZ': 'Excision of right upper lung, open approach',
    '0FBC0ZZ': 'Excision of left upper lung, open approach',
    '0FBF0ZZ': 'Excision of right lower lung, open approach',
    '0FBG0ZZ': 'Excision of left lower lung, open approach'
}

@app.route('/search', methods=['GET'])
def search_icd_code():
    code = request.args.get('code')
    if code in icd10_pcs_codes:
        return jsonify({'code': code, 'description': icd10_pcs_codes[code], 'valid': True}), 200
    else:
        return jsonify({'code': code, 'valid': False}), 404

@app.route('/validate', methods=['POST'])
def validate_icd_code():
    data = request.get_json()
    code = data.get('code')
    if code in icd10_pcs_codes:
        return jsonify({'code': code, 'description': icd10_pcs_codes[code], 'valid': True}), 200
    else:
        return jsonify({'code': code, 'valid': False}), 404

if __name__ == '__main__':
    app.run(debug=True)