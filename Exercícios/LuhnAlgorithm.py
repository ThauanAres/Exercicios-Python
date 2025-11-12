# Luhn Algorithm to verify credit card numbers.

def verify_card_number(card_number):
    # Reverse the card number (required for the Luhn algorithm)
    card_number_reversed = card_number[::-1]

    # Sum of digits in odd positions (starting from the end)
    sum_of_odd_digits = 0
    odd_digits = card_number_reversed[::2]
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    # Sum of digits in even positions (starting from the end)
    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit) * 2  # Double each even-position digit
        if number >= 10:
            # If the result is two digits, sum them (e.g., 12 → 1 + 2 = 3)
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number

    # Total sum of odd and even digits
    total = sum_of_odd_digits + sum_of_even_digits

    # Return True if the total is divisible by 10 (valid card number)
    return total % 10 == 0


def main():
    # Original card number with hyphens
    card_number = '4111-1111-4555-1142'

    # Remove hyphens and spaces from the card number
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    # Verify card validity and display the result
    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')


# Run the program
main()
