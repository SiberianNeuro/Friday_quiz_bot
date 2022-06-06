from aiogram import types


def winner_wrapper(data,):
    string = ''
    for name, username in data:
        string = string + username + ' ' + name + '\n'
    return string
