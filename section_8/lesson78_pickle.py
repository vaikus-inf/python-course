# Сериализация данных
class Character():

    def __init__(self, race, armor = 20, damage = 10):
        self.race = race
        self.armor = armor
        self.damage = damage
        self.health = 100

    def hit(self, damage):
        self.health -= damage

    def is_dead(self):
        return self.health == 0
    
    # Метод __setstate__ описывающий действия при десериализации данных
    def __setstate__(self, state):
        self.race = state.get('race', 'Elf')
        self.damage = state.get('damage', 10)
        self.armor = state.get('armor', 20)
        self.health = state.get('health', 100)

c = Character('Elf')
c.hit(10)
print(c.health)

import pickle

with open(r'E:\Dev\python-course\section_8\game_state.bin', 'w+b') as f:
    pickle.dump(c, f)

c = None
print(c)

with open(r'E:\Dev\python-course\section_8\game_state.bin', 'rb') as f:
    c = pickle.load(f)

print(c.health)
print(c.__dict__)