import time


class iter():
    def __init__(self,max_num) -> None:
        self.max_num = max_num

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        else:
            self.n3 = self.n1 + self.n2
            if self.n3 >= self.max_num:
                raise StopIteration
            else:
                self.n1, self.n2 = self.n2, self.n3
                return self.n3

if __name__ == '__main__':
    fibonacci = iter()
    for i in fibonacci:
        print(i) 
        time.sleep(0.05)



    