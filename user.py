

class User:
    def __init__(self, name, files: list[str], accesses: list[int]):
        self.name = name
        self.accesses = {key: value for key, value in zip(files, accesses)}
    def write(self, file):
        if not file in self.accesses.keys():
            print("This file doesn't exist!")
            return
        if self.name == 'admin' or self.accesses[file] & 0b010 != 0:
            with open(file, 'a') as f:
                while True:
                    line = input(">")
                    if line == 'q':
                        break
                    f.write(line + "\n")
        else:
            print('Not enough rights!')
    def read(self, file):
        if not file in self.accesses.keys():
            print("This file doesn't exist!")
            return
        if self.name == 'admin' or self.accesses[file] & 0b100 != 0:
            with open(file, 'r') as f:
                text = f.readlines()
                print()
                for i in text:
                    print(i.rstrip())
        else:
            print('Not enough rights!')
