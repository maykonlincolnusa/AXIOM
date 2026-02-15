from cryptography.fernet import Fernet
from config import SECRET_KEY

cipher = Fernet(SECRET_KEY.encode())

def encrypt_text(text: str) -> bytes:
    return cipher.encrypt(text.encode())

def decrypt_text(token: bytes) -> str:
    return cipher.decrypt(token).decode()
