from flask import Flask, request, jsonify
from cipher.ecc import ECCCipher

app = Flask(__name__)

#ECC CIPHER ALGORITHM
ecc_cipher = ECCCipher()

# ECC CIPHER ALGORITHM ENDPOINTS
@app.route('/api/ecc/generate_keys', methods=['GET'])
def ecc_generate_keys():
    ecc_cipher.generate_keys()
    return jsonify({'message': 'ECC Keys generated successfully'})

@app.route("/api/ecc/sign", methods=["POST"])
def ecc_sign_message():
    data = request.json
    message = data['message']
    private_key, _ = ecc_cipher.load_keys()
    signature = ecc_cipher.sign(message, private_key)
    import base64
    signature_b64 = base64.b64encode(signature).decode('utf-8')
    return jsonify({'signature': signature_b64})

@app.route("/api/ecc/verify", methods=["POST"])
def ecc_verify_signature():
    data = request.json
    message = data['message']
    signature_b64 = data['signature']
    _, public_key = ecc_cipher.load_keys()
    import base64
    signature = base64.b64decode(signature_b64)
    is_verified = ecc_cipher.verify(message, signature, public_key)
    return jsonify({'is_verified': is_verified})

#main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2201, debug=True)