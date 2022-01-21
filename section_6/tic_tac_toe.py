#Игра крестики-нолики
class Game:

    def __init__(self):
        self.playing_field = [i for i in range(1, 10)]
    
    def output(self):
        for i in range(1, 10):
            print(self.playing_field[i-1], end='') if i % 3 else print(self.playing_field[i-1])

    def move(self, mark):
        check = False
        while not check:
            if mark == 'X':
                square_number = int(input('Первый игрок, введите номер квадрата:'))
            else:
                square_number = int(input('Второй игрок, введите номер квадрата:'))
        
            if self.playing_field.count(square_number) == 0:
                print('Данный квадрат уже заполнен, либо введенный номер не входит в допустимый диапазон от 1 до 9')
            else:
                check = True

        self.playing_field[square_number - 1] = mark
        self.output()

    def win(self, mark):
        combo = ['012', '345', '678', '036', '147', '258', '048', '246']
        marked = ''.join([str(i) for i, v in enumerate(self.playing_field) if v == mark])
        for j in range(8):
            if marked.find(combo[j][0]) != -1 and marked.find(combo[j][1]) != -1 and marked.find(combo[j][2]) != -1:
                return True
        return False

new_game = Game()
new_game.output()

for i in range(9):
    mark = 'X' if not i % 2 else 'O'
    new_game.move(mark)
    if new_game.win(mark):
        print('Победил первый игрок!') if mark == 'X' else print('Победил второй игрок!')
        break
    if i == 8:
        print('Ничья')