def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char

    return result


def decrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 - shift) % 26 + 65)
            else:
                result += chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            result += char

    return result


print("=== Caesar Cipher Encryption & Decryption ===")

message = input("Enter Message: ")
shift = int(input("Enter Shift Key (1-25): "))

print("\n1. Encrypt")
print("2. Decrypt")

choice = input("Choose Option (1/2): ")

if choice == "1":
    encrypted_text = encrypt(message, shift)
    print("\nEncrypted Message:", encrypted_text)

elif choice == "2":
    decrypted_text = decrypt(message, shift)
    print("\nDecrypted Message:", decrypted_text)

else:
    print("Invalid Choice!")