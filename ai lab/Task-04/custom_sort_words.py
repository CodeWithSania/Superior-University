class Alpha:
    def __init__(self, input_str):
        self.words_stack = []
        self.input_str = input_str
    
    def convert(self):
        print(f"Original String: {self.input_str}")
        self.words_stack = self.input_str.split()
       
    def bubble_sort(self):
        n = len(self.words_stack)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.words_stack[j].lower() > self.words_stack[j + 1].lower():
                    self.words_stack[j], self.words_stack[j + 1] = self.words_stack[j + 1], self.words_stack[j]
        print(f"Ordered String: {' '.join(self.words_stack)}")



user_input = input("Write text: ")
alpha_instance = Alpha(user_input)
alpha_instance.convert()
alpha_instance.bubble_sort()
