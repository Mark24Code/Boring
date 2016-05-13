print("==== replace str ====")


def find_str(paragraph, word, start=0, end=None, model='one'):
    result = []
    index = 0

    paragraph = str(paragraph)
    word = str(word)
    word_len = len(word)
    head_ch = word[:1]
    if model:
        if model not in ('one', 'all'):
            raise SyntaxError("model= ['one','all']")

    if start:
        start = int(start)
        index = start
        if end:
            end = int(end)
            paragraph = paragraph[start:end]
        else:
            paragraph = paragraph[start:]

    for ch in paragraph:
        if ch == head_ch:
            begin_index = index
            end_index = index + word_len

            tmp_word = paragraph[begin_index:end_index]
            if tmp_word == word:
                result.append(index)
        index += 1
        if model == 'one' and len(result) == 1:
            break
    if result:
        if len(result) == 1:
            return result[0]
        else:
            return result
    else:
        return -1


def replace_str(paragraph, word1, word2, start=0, end=None, model='all'):
    index_list = find_str(paragraph, word1, model='all')
    word1_len = len(word1)

    slice_list = []
    for index in index_list:
        slice_list.append(index)
        slice_list.append(index+word1_len)

    head = slice[0]
    tail = slice[-1]
    slice_new = slice[1:-1]
    
if __name__ == '__main__':
    print(replace_str('THis is my word word word word', 'word', model="all"))
