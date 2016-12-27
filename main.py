# -*- coding: utf-8 -*-
import sys

sys.path.insert(0, sys.path[0]+'\\proto')
from bot_proto import *


'''
BOT_MODE
0 - standart
1 - exit
'''

BOT_MODE = 0
EXIT_MODE = False


def check_updates():
    parameters_list = telebot.get_updates()
    if EXIT_MODE:
        return 1
    if not parameters_list:
        return 0
    for parameters in parameters_list:
        run_command(*parameters)


def run_command(name, from_id, cmd, author_id, date):
    global BOT_MODE
    global EXIT_MODE

    if cmd == '/help':
        telebot.send_text(from_id, 'No help today. Sorry, %s' % name)


    elif cmd == '/exit':
        telebot.send_text_with_keyboard(from_id, 'Shut down?', [["Yes", "No"]])
        BOT_MODE = 1

    elif BOT_MODE == 1 and cmd == 'Yes':
        telebot.send_text(from_id, 'Finish by user {0}'.format(name))
        EXIT_MODE = True

    else:
        log_event('No action')
        BOT_MODE = 0
        pass

if __name__ == "__main__":
    telebot = Telegram()
    while True:
        try:
            
            # telebot.ping()
            if check_updates() != 1:
                time.sleep(telebot.Interval)
            else:
                sys.exit()
        except KeyboardInterrupt:
            print 'Interrupt by user..'
            break
