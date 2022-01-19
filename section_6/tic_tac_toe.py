class Game:

    def __init__(self):
        self.playing_field = [i for i in range(1, 10)]
        self.square_number = 0
    
    def output(self, player_number):
        if not player_number:
            self.playing_field[new_game.square_number - 1] = 'X'
        else:
            self.playing_field[new_game.square_number - 1] = 'O'
        for i in range(1, 10):
            print(self.playing_field[i-1], end='') if i % 3 else print(self.playing_field[i-1])

new_game = Game()

for i in range(9):
    if not i % 2:
        new_game.square_number = int(input('Первый игрок, введите номер квадрата:'))
    else:
        new_game.square_number = int(input('Второй игрок, введите номер квадрата:'))
    new_game.output(i % 2)