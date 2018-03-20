# basic code
def index_words(text):
    result = []
    if text:
        result.append(0)
    for idx, letter in enumerate(text):
        if letter == ' ':
            result.append(idx + 1)
    return result


address = 'Four score and seven years ago, There was a light...'
result = index_words(address)
print(result)  # first line


# more pretty code
def index_words_iter(text):
    if text:
        yield 0
    for idx, letter in enumerate(text):
        if letter == ' ':
            yield idx + 1


result = list(index_words_iter(address))
print(result)  # second line
