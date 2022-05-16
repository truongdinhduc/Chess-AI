import pygame_menu
from pygame_menu.examples import create_example_window
import pygame_menu.widgets
from typing import Tuple, Any
from mainbyHan import human_chess_color, get_level, bot1, bot2, human_vs_bot, bot_vs_bot
surface = create_example_window('Cờ vua', (512, 512))
is_human = False


def set_mode(selected: Tuple, value: Any) -> None:
    global is_human
    is_human = False if value == 1 else True
    print('is_human:', is_human)


def set_chess_color(selected: Tuple, value: Any):
    if value == 0:
       human_chess_color = True
    else:
       human_chess_color = False


def set_bot1(selected: Tuple, value: Any):
    bot1 = mainbyHan.get_leval(value)


def set_bot2(selected: Tuple, value: Any):
    mainbyHan.bot2 = mainbyHan.get_leval(value)


def start_the_game():
    if is_human:
        mainbyHan.human_vs_bot()
    else:
        mainbyHan.bot_vs_bot()


menu = pygame_menu.Menu(
    height=300,
    theme=pygame_menu.themes.THEME_BLUE,
    title='Nhập môn trí tuệ nhân tạo',
    width=512
)

menu.add.dropselect(
    title='Chọn chế độ',
    items=[('Đánh với máy ', 0),
           ('Máy với máy', 1)],
    default=0,
    font_size=16,
    selection_option_font_size=20,
    onchange=set_mode
)
menu.add.dropselect(
    title='Chọn màu cờ',
    items=[('Trắng: đi trước', 0),
           ('Đen: đi sau', 1)],
    default=0,
    font_size=16,
    selection_option_font_size=20,
    onchange=set_chess_color
)
menu.add.dropselect(
    title='Độ khó BOT 1',
    items=[('Dễ', 0),
           ('Trung bình', 1),
           ('Khó', 2), ],
    default=0,
    font_size=16,
    selection_option_font_size=20,
    onchange=set_bot1
)
menu.add.dropselect(
    title='Độ khó BOT 2',
    items=[('Dễ', 0),
           ('Trung bình', 1),
           ('Khó', 2), ],
    default=0,
    font_size=16,
    selection_option_font_size=20,
    onchange=set_bot2
)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)


def cont():
    menu.mainloop(surface)


cont()
