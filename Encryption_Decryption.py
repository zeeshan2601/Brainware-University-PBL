# Simple Encryption and Decryption Tool
def encrypt(text, key):
    result = ""
    for char in text:
        result = result + chr(ord(char) ^ key)
    return result

def decrypt(text, key):
    result = ""
    for char in text:
        result = result + chr(ord(char) ^ key)
    return result

print("1. Encrypt")
print("2. Decrypt")

choice = input("Enter choice: ")
text = input("Enter text: ")
key = int(input("Enter key: "))

if choice == "1":
    encrypted = encrypt(text, key)
    print("Encrypted text:", encrypted)

elif choice == "2":
    decrypted = decrypt(text, key)
    print("Decrypted text:", decrypted)
    
else:
    print("Invalid choice")