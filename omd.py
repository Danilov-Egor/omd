# Guido van Rossum <guido@python.org>
import random


def step2_umbrella():
    """
    What happens if the duck takes an umbrella
    """
    
    # погода на улице
    weather_opt = ['пошёл дождь', 'солнечно☀️', 'дует сильный ветер 🌬', 'черт знает что']
    weather = random.choice(weather_opt)
    
    # вывод в консоль
    print(f"На улице {weather}!", end=" ")
    
    if weather == 'пошёл дождь':
        print('Не зря взяли зонтик! Уточка довольна 🦆☔️')

    elif weather == 'солнечно☀️':
        print('"Зря зонтик взяла!" - подумала утка и приуныла')
        
    elif weather == 'дует сильный ветер 🌬':
        print('Мэрри Поппинс отдыхает... Уиии 🦆')
        
    else:
        print('Утка не имеет ясного ответа.')
    

def step2_no_umbrella():
    """
    What happens if the duck doesn't take an umbrella
    """
    print(f'Уточка вышла из дома и пошла гулять, {6*"ля "}')
    
    option = random.randint(1, 4)
    i = 0
    while i != option:
        print('Утка-маляр радостно гуляет...')
        i += 1
    print('Пока вдруг не вспомнила, что завтра понедельник и никакой зонтик ее не спасет 😩')
    

def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    
    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


if __name__ == '__main__':
    step1()
