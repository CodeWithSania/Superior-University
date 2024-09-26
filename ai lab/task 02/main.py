class Player:
    def __init__(self, name):
        self.name = name

    def say_number(self, number):
        if number % 3 == 0 and number % 5 == 0:
            return "Fizz Buzz"
        elif number % 3 == 0:
            return "Fizz"
        elif number % 5 == 0:
            return "Buzz"
        else:
            return str(number)


class Game:
    def __init__(self, players, upper_limit):
        self.players = players
        self.upper_limit = upper_limit
        self.current_player_index = 0

    def play(self):
        for number in range(1, self.upper_limit + 1):
            current_player = self.players[self.current_player_index]
            expected_output = current_player.say_number(number)

            print(f"{current_player.name}: {expected_output}")

            # Move to the next player
            self.current_player_index = (self.current_player_index + 1) % len(self.players)



player_names = input("Enter player names separated by commas: ").split(',')
players = [Player(name.strip()) for name in player_names]
upper_limit = int(input("Enter the upper limit for the Fizz Buzz game: "))
game = Game(players, upper_limit)
game.play()
