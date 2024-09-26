class PunctuationRemover:
    def __init__(self, input_str):
        self.input_str = input_str
        self.punctuation_list = ['.', ',', '?', '!', ':', ';', "'", '"', '(', ')', '[', ']', '{', '}', '-', '–', '—', '...', '/', '\\', '|']

    def remove_punctuations(self):
        result_list = []
        for character in self.input_str:
            if character in self.punctuation_list:
                continue
            result_list.append(character)
        
        output_string = ''.join(result_list)
        print(output_string)



user_input = input("Enter Your String: ")
remover = PunctuationRemover(user_input)
remover.remove_punctuations()
