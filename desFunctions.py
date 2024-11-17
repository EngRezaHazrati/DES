from desRequiredTables import *
import base64

def str_to_bin(user_input):
    # Convert the string to binary

    binary_representation = ''
    
    for char in user_input:
        # Get ASCII value of the character and convert it to binary
        binary_char = format(ord(char), '08b')
        binary_representation += binary_char
        binary_representation = binary_representation[:64]
    
    # Pad or truncate the binary representation to 64 bits
    binary_representation = binary_representation[:64].ljust(64, '0')
    
    return binary_representation

######################################################################

def binary_to_ascii(binary_str):
    # Conversion of the Binary to ASCII

    ascii_str = ''.join([chr(int(binary_str[i:i+8], 2)) for i in range(0, len(binary_str), 8)])

    return ascii_str

######################################################################

def ip_on_binary_rep(binary_representation):
    # Implementation of Initial Permutation on the Binary string

    ip_result = [None] * 64
    
    for i in range(64):
        ip_result[i] = binary_representation[ip_table[i] - 1]

    # Convert the result back to a string for better visualization
    ip_result_str = ''.join(ip_result)
    
    return ip_result_str

######################################################################

def key_in_binary_conv(main_Key):
    # Function to represent the Key in the Binary format

    binary_representation_key = ''

    for char in main_Key[:8]:
    # Convert the characters to binary and concatenate to form a 64-bit binary string
        binary_key = format(ord(char), '08b') 
        binary_representation_key += binary_key

    return binary_representation_key

######################################################################

def generate_round_keys(main_key):
    # This function is responsible to Generate a Key for each Round and save the Key in a List

    # Key into binary
    binary_representation_key = key_in_binary_conv(main_key)
    pc1_key_str = ''.join(binary_representation_key[bit - 1] for bit in pc1_table)

    
    # Split the 56-bit key into two 28-bit halves
    c0 = pc1_key_str[:28]
    d0 = pc1_key_str[28:]
    round_keys = []
    for round_num in range(16):
        # Perform left circular shift on C and D
        c0 = c0[shift_schedule[round_num]:] + c0[:shift_schedule[round_num]]
        d0 = d0[shift_schedule[round_num]:] + d0[:shift_schedule[round_num]]
        # Concatenate C and D
        cd_concatenated = c0 + d0

        # Apply the PC2 permutation
        round_key = ''.join(cd_concatenated[bit - 1] for bit in pc2_table)

        # Store the round key
        round_keys.append(round_key)
    return round_keys

######################################################################

