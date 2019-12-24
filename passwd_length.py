import Generators as gen
from datetime import datetime
import csv

letters_numbers_list = []


def main():
    global letters_numbers_list
    out = open('password_generation_logs.csv', 'a+')
    out.write('\nGenerated Password' + ','+'Date and Time\n')
    pass_len = int(input("Enter How many characters do you want in your password: "))

    if pass_len < 6:
        print("Password Should have minimum 6 characters in it.")
        exit(0)

    word_len = int(input("Enter How many letters do you want in your password:"))
    letters_numbers_list += gen.gen_letters(word_len)

    numbers_len = int(input("Enter How many numbers do you want in your password:"))

    letters_numbers_list += gen.gen_numbers(numbers_len)
    # print(map(str, gen.gen_numbers(numbers_len)))

    if pass_len != (word_len + numbers_len):
        print("The Password Length and (Words & Numbers Length) should be match.")
        exit(0)

    # print(letters_numbers_list)
    list_after_shuffle = gen.shuffle_list(letters_numbers_list)

    # print(list_after_shuffle)
    # print(gen.converting_list_in_string(list_after_shuffle) + ' ', end='')
    # print(datetime.now())

    # [str(gen.converting_list_in_string(list_after_shuffle)), str(datetime.now())]
    #
    # with open('password_generation_logs.csv', 'w+') as csvfile:
    #     filewriter = csv.writer(csvfile, delimiter=',',
    #                             quoting=csv.QUOTE_MINIMAL)
    #     filewriter.writerow([gen.converting_list_in_string(list_after_shuffle),datetime.now()])
    #     # filewriter.writerow([])

    out.write(gen.converting_list_in_string(list_after_shuffle) +','+ str(datetime.now()))
    # out.write('\n')
    out.close()
    # filewriter.writerow([])


if __name__ == "__main__":
    main()