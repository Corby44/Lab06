# 3502C Lab 6 Code
# Written by: Michael Muraglia
# 7/19/2023

def encode(password):  # function to encode password
    encoded = ""  # encoded password variable
    for integer in password:  # gates used to catch password integer and add 3
        if integer == '0':
            encoded += '3'
        elif integer == '1':
            encoded += '4'
        elif integer == '2':
            encoded += '5'
        elif integer == '3':
            encoded += '6'
        elif integer == '4':
            encoded += '7'
        elif integer == '5':
            encoded += '8'
        elif integer == '6':
            encoded += '9'
        elif integer == '7':
            encoded += '0'
        elif integer == '8':
            encoded += '1'
        else:
            encoded += '2'
    return encoded
#Decode Portion added By Mohamed L Afia
def decode_pass(password):
    decoded_pass =""
    for digit in password:
        decoded_dig = str((int(digit)-3))
        decoded_pass += decoded_dig
    return decoded_pass
def main():
    while True:
        print('Menu')  # menu options
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit\n')

        user_input = int(input("Please enter an option: "))  # user select menu options

        if user_input == 1:  # user enters password and program encodes
            user_password = input('Please enter your password to encode: ')
            encoded_password = encode(user_password)
            print('Your password has been encoded and stored!\n')
        elif user_input == 2:  # user wants password decoded - displays encoded and decoded password
            decoded_password = decode_pass(encoded_password)
            print(f'The encoded password is {encoded_password}, and the original password is {decoded_password}.\n')
        elif user_input == 3:  # terminates program
            break


if __name__ == "__main__":
    main()
