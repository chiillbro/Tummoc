def validate_credit_card(cc_number):
    cc_str = str(cc_number)
    length = len(cc_str)

    if length not in [13, 15, 16]:
        return False
    if not (cc_str.startswith('4') or cc_str.startswith('5') or cc_str.startswith('37') or cc_str.startswith('6')):
        return False
    if cc_str.startswith('4') and length != 13:
        return False
    if cc_str.startswith('5') and length != 13:
        return False
    if cc_str.startswith('37') and length != 16:
        return False
    if cc_str.startswith('6') and length != 15:
        return False
    
    total = 0
    reverse_digits = cc_str[::-1]

    for i in range(length):
        digit = int(reverse_digits[i])
        if i % 2 == 1:
            doubled_digit = digit * 2
            total += doubled_digit // 10 + doubled_digit % 10
        else:
            total += digit

    return total % 10 == 0

def main():
    try:
        card_number = int(input("Enter a credit card number: "))
        if validate_credit_card(card_number):
            print("The card number is valid.")
        else:
            print("The card number is invalid.")
    except ValueError:
        print("Invalid input. Please enter a valid long integer credit card number.")

if __name__ == "__main__":
    main()