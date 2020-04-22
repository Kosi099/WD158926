class Samogloski:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        for i in range(self.index):
            if('self.data[self.index]==a'' or 'self.data[self.index]=='e''or'self.data[self.index]=='i'' or 'self.data[self.index]=='o''or'self.data[self.index]=='u'' or 'self.data[self.index]=='y''):
                return self.data[self.index] 
        raise StopIteration
        