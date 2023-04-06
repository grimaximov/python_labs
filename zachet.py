field_num = 3
field = [1,2,3,4,5,6,7,8,9]

def draw_field():
    print('_' * 4 * field_num)
    for i in range(field_num):
        # print(('' * 3 + '|') *3)
        print('', field[i*3], '|', field[1+i*3], '|', field[2+i*3],'|')
        print(('_'*3+'|')*3)

def game_step(index, char):
    if (index>9 or index<1 or field[index-1] in ('X','O')):
        return False
    field[index-1]=char
    return True

def check_end():
    end = False
    win_line = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for i in win_line:
        if(field[i[0]]==field[i[1]] and
        field[i[1]]==field[i[2]]):
            return field[i[0]]
        # return  end


def start_game():
    player = 'X'
    step = 1
    draw_field()
    while(step<10) and (check_end()==False):
        gamer_step = int(input('Сейчас ходит игрок'+player+' Введите номер поля: '))
        if(game_step(gamer_step, player)):
            print("Вы сделали ход!")
            if (player=='X'):
                player='O'
            else:
                player= 'X'
            draw_field()
            step+=1
        else:
            print('Такой ход невозможен!')
            # print("Выиграл"+check_end())



print('ЗачОтные крестики-нолики')
start_game()