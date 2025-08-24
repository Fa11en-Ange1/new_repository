#5
class DictKeysIterator:
    def __init__(self, dictionar):
        self.keys = list(dictionar.keys())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.keys):
            key_1 = self.keys[self.index]
            self.index += 1
            return key_1
        else:
            raise StopIteration


dictionary = {"a": 1, "b": 2, "c": 3}
dict_iter = DictKeysIterator(dictionary)
for key in dict_iter:
    print(key)


#6
def even_number_filter(number):
    for num in number:
        if num % 2 == 0:
            yield num


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_nums = even_number_filter(numbers)
for num in even_nums:
    print(num)
