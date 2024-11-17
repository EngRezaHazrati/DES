from desFunctions import *

def encryption(user_input, main_key):
    # This function is responsible to implement the Encryption process in DES algorithm
    # Plain-Text -> Cipher-Text

    binary_rep_of_input = str_to_bin(user_input)
    # Initialize lists to store round keys
    round_keys = generate_round_keys(main_key)

    ip_result_str = ip_on_binary_rep(binary_rep_of_input)


    # the initial permutation result is devided into 2 halfs
    lpt = ip_result_str[:32]
    rpt = ip_result_str[32:]


    # Assume 'rpt' is the 32-bit right half, 'lpt' is the 32-bit left half,
    # and 'round_keys' is a list of 16 round keys

    for round_num in range(16):
        # Perform expansion (32 bits to 48 bits)
        expanded_result = [rpt[i - 1] for i in e_box_table]

        # Convert the result back to a string for better visualization
        expanded_result_str = ''.join(expanded_result)

        # Round key for the current round
        round_key_str = round_keys[round_num]

        print()
        print(f"Round {round_num+1}:")
        print("Subkey: ", round_key_str)
        print("Output: ", lpt+rpt)
        

        xor_result_str = ''
        for i in range(48):
            xor_result_str += str(int(expanded_result_str[i]) ^ int(round_key_str[i]))


        # Split the 48-bit string into 8 groups of 6 bits each
        six_bit_groups = [xor_result_str[i:i+6] for i in range(0, 48, 6)]

        # Initialize the substituted bits string
        s_box_substituted = ''

        # Apply S-box substitution for each 6-bit group
        for i in range(8):
            # Extract the row and column bits
            row_bits = int(six_bit_groups[i][0] + six_bit_groups[i][-1], 2)
            col_bits = int(six_bit_groups[i][1:-1], 2)

            # Lookup the S-box value
            s_box_value = s_boxes[i][row_bits][col_bits]
            
            # Convert the S-box value to a 4-bit binary string and append to the result
            s_box_substituted += format(s_box_value, '04b')

        # Apply a P permutation to the result
        p_box_result = [s_box_substituted[i - 1] for i in p_box_table]

        # # Convert the result back to a string for better visualization
        # p_box_result_str = ''.join(p_box_result)


        # Convert LPT to a list of bits for the XOR operation
        lpt_list = list(lpt)

        # Perform XOR operation
        new_rpt = [str(int(lpt_list[i]) ^ int(p_box_result[i])) for i in range(32)]

        # Convert the result back to a string for better visualization
        new_rpt_str = ''.join(new_rpt)

        # Update LPT and RPT for the next round
        lpt = rpt
        rpt = new_rpt_str

        # Print or use the RPT for each round

    print('\n')
    # At this point, 'lpt' and 'rpt' contain the final left and right halves after 16 rounds

    # After the final round, reverse the last swap
    final_result = rpt + lpt

    # Perform the final permutation (IP-1)
    final_cipher = [final_result[ip_inverse_table[i] - 1] for i in range(64)]

    # Convert the result back to a string for better visualization
    final_cipher_str = ''.join(final_cipher)

    # Print or use the final cipher(binary)
    # print("Final Cipher binary:", final_cipher_str, len(final_cipher_str))


    # Convert binary cipher to ascii
    final_cipher_ascii = binary_to_ascii(final_cipher_str)
    #print("Final Cipher text:", final_cipher_ascii , len(final_cipher_ascii))
    
    return final_cipher_ascii