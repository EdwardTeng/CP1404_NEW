def count_word_freq(input_string):

    input_string_list = input_string.split()
    input_string_list_2 = []

    for i in input_string_list:

        if i not in input_string_list_2:
            input_string_list_2.append(i)

    for i in range(0, len(input_string_list_2)):
        print(" {} : {}".format(input_string_list_2[i], input_string_list.count(input_string_list_2[i])))

def main():
    input_string = str(input("Text: "))
    count_word_freq(input_string)


if __name__=="__main__":
    main()