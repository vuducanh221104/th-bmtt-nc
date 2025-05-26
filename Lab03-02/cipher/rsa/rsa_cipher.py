import os
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

KEY_FOLDER = os.path.join(os.path.dirname(__file__), 'keys')
PRIVATE_KEY_PATH = os.path.join(KEY_FOLDER, 'privateKey.pem')
PUBLIC_KEY_PATH = os.path.join(KEY_FOLDER, 'publicKey.pem')


class RSACipher:
    def __init__(self):
        if not os.path.exists(KEY_FOLDER):
            os.makedirs(KEY_FOLDER)

    def generate_keys(self):
        key = RSA.generate(2048)
        private_key = key.export_key()
        public_key = key.publickey().export_key()

        with open(PRIVATE_KEY_PATH, 'wb') as f:
            f.write(private_key)

        with open(PUBLIC_KEY_PATH, 'wb') as f:
            f.write(public_key)

        return {
            "message": "Keys generated successfully",
            "private_key_path": PRIVATE_KEY_PATH,
            "public_key_path": PUBLIC_KEY_PATH
        }

    def encrypt(self, message):
        with open(PUBLIC_KEY_PATH, 'rb') as f:
            public_key = RSA.import_key(f.read())
        cipher = PKCS1_OAEP.new(public_key)
        encrypted_message = cipher.encrypt(message.encode('utf-8'))
        return base64.b64encode(encrypted_message).decode('utf-8')

    def decrypt(self, ciphertext):
        with open(PRIVATE_KEY_PATH, 'rb') as f:
            private_key = RSA.import_key(f.read())
        cipher = PKCS1_OAEP.new(private_key)
        decoded_data = base64.b64decode(ciphertext)
        decrypted_message = cipher.decrypt(decoded_data)
        return decrypted_message.decode('utf-8')

    def sign(self, message):
        with open(PRIVATE_KEY_PATH, 'rb') as f:
            private_key = RSA.import_key(f.read())
        h = SHA256.new(message.encode('utf-8'))
        signature = pkcs1_15.new(private_key).sign(h)
        return base64.b64encode(signature).decode('utf-8')

    def verify(self, message, signature):
        with open(PUBLIC_KEY_PATH, 'rb') as f:
            public_key = RSA.import_key(f.read())
        h = SHA256.new(message.encode('utf-8'))
        try:
            pkcs1_15.new(public_key).verify(h, base64.b64decode(signature))
            return True
        except (ValueError, TypeError):
            return False
