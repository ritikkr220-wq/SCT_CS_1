def caesar_cipher(text, shift):
    result = ""
    shift = shift % 26

    for ch in text:
        if ch.isupper():
            result += chr((ord(ch) - 65 + shift) % 26 + 65)
        elif ch.islower():
            result += chr((ord(ch) - 97 + shift) % 26 + 97)
        else:
            result += ch   # spaces and symbols unchanged
    return result


# User Input
message = input("Enter the message: ")
shift = int(input("Enter shift value: "))
mode = input("E: Encryption or D: Decryption : ").upper()

if mode == "E":
    encrypted = caesar_cipher(message, shift)
    print("Encrypted Message:", encrypted)

elif mode == "D":
    decrypted = caesar_cipher(message, -shift)
    print("Decrypted Message:", decrypted)

else:
    print("Invalid Choice")
