from desEncryption import *
from desDecryption import *


# Start
des_process = ""
while (des_process == "") or (not (des_process in ["1","2"])):
    print("Please select the process you would like to perform:")
    print("[1] DES algorithm Encryption")
    print("[2] DES algorithm Decryption")
    print("Your Choice [1 | 2]: ", end="")
    des_process = input()


main_key = "244328902"

# This would be 56 bits. If longer string be entered, the system will truncate it to have 56 bits wide
plain_text = "Hello To" 

match des_process:
    case "1":
        # Encryption process is selected

        # Student ID = 244328902
        plain_text = input("Enter a string as plain text: ")
        main_key = input("Enter your main key: ")
        
        cipher_text = encryption(plain_text, main_key)
        cipher_text_base64 = base64.b64encode(cipher_text.encode()).decode()

        print()
        print("Plain text: \t", plain_text)
        print("Cipher text: \t", cipher_text_base64)
        print()


    case "2":
        # Decryption process is selected

        cipher_text_base64 = input("Enter a string as cipher text: ")
        cipher_text = base64.b64decode(cipher_text_base64).decode()

        main_key = input("Enter your main key: ")

        plain_text = decryption(cipher_text, main_key)

        print()
        print("Cipher text: \t", cipher_text_base64)
        print("Plain text: \t", plain_text)
        print()
