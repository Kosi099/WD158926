class Wspak:
    """Iterator zwracający wartości w odwróconym porządku"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        yield self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        if self.index%2==0:
            yield self.data[self.index]