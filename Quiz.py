from correctinput import Correctinput

from prettytable import PrettyTable

import os


'''*************************************[FUNCTIONS]**********************************************'''

def txt_decoder(file):
    '''TXT to DICT decoder ,Output as a python dict.'''
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the file path
    file_path = os.path.join(current_dir, 'questions', file_name)
    with open(file_path, 'r') as read_dict:
        Q_data = eval(read_dict.read())
        # read_dict.close()
        return Q_data


class Quiz:
    '''Quiz data passed as a dict'''
    def quiz(self, Q_data):
        
        points = 0
        for i in Q_data:
            list_opt = []
            for m in Q_data[i]:
                if m == 'Options':
                    for y in Q_data[i][m]:
                        list_opt.append(Q_data[i][m][y])
                elif m == 'Type':
                    t = Q_data[i][m]
                elif m == 'Answer':
                    a = Q_data[i][m]
                else:
                    q = Q_data[i][m]
            
            if t == 'FILL_BLANKS':
                print(f'{q}\n"__________"')
            elif t == 'T-F':
                print(f'{q}\n{list_opt}')
            else:
                print(f'{q}\n{list_opt}')
            user_input = input('Choose the correct one >').upper()
            
            if user_input == a:
                points += 1 
                print(f'Correct answer!\n+1  Current Score {points}')
            else:
                if points > 0:
                    points -= 1 
                print(f'Wrong answer!\n-1 Current Score {points}')
                
        pass

'''*************************************[INPUT]******************************************'''
table = PrettyTable()
test_input = Correctinput()

file_ = input('File name:\nto import\n')
file_name = file_ + '.txt'

Data = txt_decoder(file_name)
test_results = Quiz()
results = test_results.quiz(Data)
