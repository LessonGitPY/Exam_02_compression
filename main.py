SPLIT = "&^&"


def compress_file_to_file(file_name_1, file_name_2, key_dict_symbols):
    with open(file_name_1, "r", encoding="utf-8") as f:
        text_without_compression = f.read()

    text_compression = ""
    for i in text_without_compression:
        text_compression += str(v[i])

    with open(file_name_2, "w", encoding="utf-8") as f:
        f.write("".join(i + SPLIT if i != "\n" else "\\n" + SPLIT for i in key_dict_symbols) + "\n")
        f.write(text_compression)

    return True


def decompression(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        head_line = f.readline()
        if head_line[-1:] == "\n":
            head_line = head_line[:-1 - len(SPLIT)]  # убираем перенос строки и последний разделитель
        dict_symbols = create_dict_symbols_for_key_nums(head_line.split(SPLIT))
        print(dict_symbols)

        text = f.read()
        text_2 = ""
        for number in text:
            text_2 += dict_symbols[number]

        return text_2


def create_dict_symbols_for_key_nums(symbols):
    dict_code_symbol_f = {}

    for number, key in enumerate(symbols):
        dict_code_symbol_f[str(number)] = key
    return dict_code_symbol_f


def create_dict_symbols(symbols):
    dict_code_symbol_f = {}

    for number, key in enumerate(symbols):
        dict_code_symbol_f[key] = number
    return dict_code_symbol_f


def analysing_text(text):
    dict_symbols = {}

    for i in text:
        if i in dict_symbols:
            dict_symbols[i] += 1
        elif i not in dict_symbols:
            dict_symbols[i] = 1

    return dict_symbols


def sorted_dict(dict_symbols):
    sorted_values = sorted(dict_symbols.values(), reverse=True)  # Сортировка словаря Python по значению
    new_sorted_dict = {}

    for i in sorted_values:
        for k in dict_symbols.keys():
            if dict_symbols[k] == i:
                new_sorted_dict[k] = dict_symbols[k]
                del dict_symbols[k]
                break
    return new_sorted_dict


if __name__ == '__main__':
    with open("text.txt", "r", encoding="utf-8") as f:
        text = f.read()
    d = analysing_text(text)
    print(d)
    d = sorted_dict(d)
    print(d)
    v = create_dict_symbols(d.keys())
    print(v)
    compress_file_to_file("text.txt", "text_2.txt", v.keys())
    print("Сжатие завершено!")
    text = decompression("text_2.txt")
    print(text)






    # def create_dict_symbols_ru():
    #     dict_code_symbol_f = {}
    #     for i in range(64):  # 63
    #         dict_code_symbol_f[chr(i+1040)] = i
    #     return dict_code_symbol_f
    # dict_code_symbol = create_dict_symbols_ru()
    # print(ord("А"))
    # print(dict_code_symbol)
    #
    # text_1 = "приветеТ"
    # text_1_bin = bin(int.from_bytes(text_1.encode(), 'big'))
    # print(type(text_1_bin))
    # print(text_1_bin, text_1)
    #
    # text_1_compression = ""
    # for i in text_1:
    #     if i in dict_code_symbol:
    #         text_1_compression += str(dict_code_symbol[i])
    #     else:
    #         text_1_compression += i
    # print(text_1, sys.getsizeof(text_1) - 49)
    # print(text_1_bin, sys.getsizeof(text_1_bin) - 49)
    # print(int(text_1_bin[2:]), sys.getsizeof(int(text_1_bin[2:])) - 49)
    # print(text_1_compression, sys.getsizeof(text_1_compression) - 49)
    # text_1_int = "00000000"
    # print(text_1_int, sys.getsizeof(text_1_int) - 49)
    # text_1_int = "11111111"
    # print(text_1_int, sys.getsizeof(text_1_int) - 49)
    # text_1_int = "22222222"
    # print(text_1_int, sys.getsizeof(text_1_int) - 49)
    # text_1_int = "99999999"
    # print(text_1_int, sys.getsizeof(text_1_int) - 49)

    # text = 'hello1'
    # t2b = int.from_bytes(text.encode(), 'big')
    # print(t2b)
    # n = int(t2b, 2)
    # b2t = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
    # print(b2t)