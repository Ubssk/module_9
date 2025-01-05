class StepValueError(ValueError):
    pass

class Iterator:
    def __init__(self, start, stop, step=1):
        self.start = start - step
        self.stop = stop
        self.step = step
        if self.step ==0:
            raise StepValueError()

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        self.pointer += self.step
        if self.step > 0:
            if self.pointer<=self.stop:
                return self.pointer
        elif self.step < 0:
            if self.pointer>=self.stop:
                return self.pointer
        raise StopIteration()


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
    print('iter1')

except StepValueError:
    print('Шаг не может быть равен 0')

try:
    iter2 = Iterator(-5, 1)
    for i in iter2:
        print(i, end=' ')
    print('iter2')
except StepValueError:
    print('Шаг не может быть равен 0')

try:
    iter3 = Iterator(6, 15, 2)
    for i in iter3:
        print(i, end=' ')
    print('iter3')
except StepValueError:
    print('Шаг не может быть равен 0')


try:
    iter4 = Iterator(5, 1, -1)
    for i in iter4:
        print(i, end=' ')
    print('iter4')
except StepValueError:
    print('Шаг не может быть равен 0')

try:
    iter5 = Iterator(10, 1)
    for i in iter5:
        print(i, end=' ')
    print('iter5')
except StepValueError:
    print('Шаг не может быть равен 0')
