# Импорт модуля из пакета
#from MainPackage import main_script
#from MainPackage.SubPackage import subscript

# Импорт конкретной функции из модуля subscript:
#from MainPackage.SubPackage.subscript import hello_subscript

# Импорт модуля main_script как main:
from MainPackage import main_script as main

# Импорт всех функций из модуля subscript:
from MainPackage.SubPackage.subscript import *

#main_script.hello_main()
#subscript.hello_subscript()
# Или:
main.hello_main()
hello_subscript()
hello_indeed()

