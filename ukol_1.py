def word_chain(words):
    return max(chain(str(word), words - {word}) for word in words) if words is not None and words != {} else 0


def check_word(word):
    return True if word is not None and len(word) > 0 else False


def chain(current_word, words):
    chain_length = 1
    for word in words:
        word = str(word)
        if check_word(current_word) and check_word(str(word)) and current_word[-1] == str(word)[0]:
            chain_length = max(chain_length, 1 + chain(str(word), words - {word}))
    return chain_length


test_sets = [{}, {''}, None, {None, 'red'}, {'red'}, {2563, 'elephant', 'tiger', 'robot', 'train'},
             {'cat', 'mouse', 'elephant', 'ham', 'moose'}, {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'},
             {'red', '', None, 'blue', 52856, 'elephant'}]

for test in test_sets:
    print("Testing set " + str(test) + ". Maximum chain length: " + str(word_chain(test)))