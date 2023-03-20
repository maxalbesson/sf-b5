# field for game
field = [['-'] * 3 for _ in range(3)]


def show_field():
    print('  0 1 2')
    for i in range(len(field)):
        print(str(i), *field[i])


# users data
x = None
y = None


def users_data(func):
    global x, y
    while True:
        data = input('Введите 2 координаты: ').split()
        if len(data) != 2:
            print('Введено неправильное количество координат.')
            continue
        if not (data[0].isdigit() and data[1].isdigit()):
            print('Координаты должны содержать только числа')
            continue
        x, y = map(int, data)
        if not(0 <= x < 3 and 0 <= y < 3):
            print('Превышен диапазон координат')
            continue
        # if len(data[0]) and len(data[1]) != 1:
        #     print('Должно быть однозначное число')
        #     continue
        if func[x][y] != '-':
            print('Ячейка уже занята!')
            continue
        break
    return x, y


# requests
def the_game():
    count = 0
    while True:
        if count % 2 == 0:
            user = 'x'
        else:
            user = 'o'
        show_field()
        x, y = users_data(field)
        field[x][y] = user
        if count == 8:
            print('Ничья')
            show_field()
            break
        if check_win(field, user):
            print(f'Игрок "{user}" победил!!!')
            show_field()
            break
        count += 1
        print('Ход: ', count)


# win_case
def check_win(func, user):
    def diagonal(pos1, pos2, pos3, user):
        if pos1 == user and pos2 == user and pos3 == user:
            return True
    for i in range(3):
        if diagonal(func[i][0], func[i][1], func[i][2], user) or \
                diagonal(func[0][i], func[1][i], func[2][i], user) or \
                diagonal(func[0][0], func[1][1], func[2][2], user) or \
                diagonal(func[2][0], func[1][1], func[0][2], user):
            return True
    return False


start = input('Нажмите Enter для запуска игры.')
the_game()
