from cryptography.fernet import Fernet
key = Fernet.generate_key()
with open("Secret.key","wb") as key_file:
    key_file.write(key)
    
    
print("Encryption key has been generated and saved to Secret.key")