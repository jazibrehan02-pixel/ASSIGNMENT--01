# Encryption Function
def caesar_encrypt(text, shift):
    result = ""

    for char in text:
        # Check if character is uppercase letter
        if char.isupper():
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))

        # Check if character is lowercase letter
        elif char.islower():
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))

        # Keep spaces and special characters same
        else:
            result += char

    return result


# Decryption Function
def caesar_decrypt(ciphertext, shift):
    result = ""

    for char in ciphertext:
        if char.isupper():
            result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))

        elif char.islower():
            result += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))

        else:
            result += char

    return result


# Main Program
text = input("Enter message: ")
shift = int(input("Enter shift value: "))

encrypted = caesar_encrypt(text, shift)
print("Encrypted Message:", encrypted)

decrypted = caesar_decrypt(encrypted, shift)
print("Decrypted Message:", decrypted)