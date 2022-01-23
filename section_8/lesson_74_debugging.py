# Импорт модуля отладки
import pdb

x = 1
y = 2

# Точка останова
pdb.set_trace()

z = 3
x += 1

# Точка останова
pdb.set_trace()

print('finish')