from cryptography.fernet import Fernet
import base64
class EncryptionService:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)
    def encrypt(self, text):
        encrypted_text = self.cipher_suite.encrypt(text.encode())
        return base64.urlsafe_b64encode(encrypted_text).decode()
    def decrypt(self, encoded_text):
        encrypted_text_bytes = base64.urlsafe_b64decode(encoded_text)
        return self.cipher_suite.decrypt(encrypted_text_bytes).decode()
encryption_service = EncryptionService()