import string as gen_str
import random as rand


def gen_letters(letters_len):
    letters_list = []
    letters_str = gen_str.ascii_letters
    for i in range(0, letters_len):
        letters_list.append(rand.choice(letters_str))
    rand.shuffle(letters_list)
    return letters_list


def gen_numbers(numbers_len):
    numbers_list = []
    for i in range(0, numbers_len):
        numbers_list.append(rand.randrange(0, 9))
    rand.shuffle(numbers_list)
    return numbers_list


def shuffle_list(list_for_shuffle):
    rand.shuffle(list_for_shuffle)
    return list_for_shuffle


def converting_list_in_string(shuffle_list):
    str1 =''
    for i in shuffle_list:
        str1 += str(i)
    return str1



