from os import system
class Correctinput: 
    '''correctinput(msgg , x):__
    msgg -> messege to display,
    x -> Expected input, taken as a list.
    '''
    def correctinput(self, msgg ,x):
        input_1 = input(f'{msgg} {x}\n').upper()
        if isinstance(x[0], str):
            while input_1 not in x:
                input_1 = input('Invalid input!\n').upper()
        else:
            input_1 = int(input_1)
            while input_1 not in x:
                input_1 = int(input('Invalid input!\n'))
        system('cls')
        return input_1
            

