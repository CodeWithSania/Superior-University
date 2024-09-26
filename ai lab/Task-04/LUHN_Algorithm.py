class VisaCard:
    def __init__(self):
        self.card_digits = [5, 5, 9, 0, 4, 9, 0, 2, 1, 5, 9, 0, 0, 7, 1, 1]
        self.last_digit = ''

    def remove_last_digit(self):
        self.last_digit = self.card_digits.pop()

    def reverse_digits(self):
        self.card_digits = self.card_digits[::-1]

    def double_even_positions(self):
        modified_digits = []
        for index in range(len(self.card_digits)):
            if index % 2 == 0:
                modified_digits.append(self.card_digits[index] * 2)
            else:
                modified_digits.append(self.card_digits[index])
        self.card_digits = modified_digits

    def subtract_nine(self):
        for i in range(len(self.card_digits)):
            if self.card_digits[i] > 9:
                self.card_digits[i] -= 9
        self.card_digits.append(self.last_digit)

    def validate_card(self):
        total_sum = sum(self.card_digits)
        if total_sum % 10 == 0:
            print("Valid Card")
        else:
            print("Not Valid Card")



card = VisaCard()
card.remove_last_digit()
card.reverse_digits()
card.double_even_positions()
card.subtract_nine()
card.validate_card()
