def words(string_words):

    word_list = []
    if ' ' in string_words:

        word_list = [i for i in string_words.split() if i]
    elif '\n' in string_words:
        word_list = string_words.split('\n')
    elif '\t' in string_words:
        word_list = string_words.split('\t')
    else:
        return {string_words : 1}

    for i in range(len(word_list)):
        try:
            word_list[i] = int(word_list[i])
        except ValueError:
            continue

    my_dict = {}
    for w in word_list:
        my_dict.setdefault(w, 0)
        my_dict[w] += 1
    return my_dict