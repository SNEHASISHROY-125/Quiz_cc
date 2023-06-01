import save_Q_data_input
import correctinput
import os
Question_dict = {}
Q_no = 0
# How_many_Q = int(input('How many do you want to create? \n> '))

input1_numeric= correctinput.Correctinput()
input2_str_type= correctinput.Correctinput()
input3_str_answ_abcd= correctinput.Correctinput()
input3_str_answ_tf= correctinput.Correctinput()

How_many_Q = input1_numeric.correctinput('How many do you want to create?', range(1,100))

def data_input():
    Q_x = {}  # Create a new empty dictionary for each question
    question = input('Type your question > ').upper()
    
    type = input2_str_type.correctinput('Set mode:\n', ['MCQ','T-F','FILL_BLANKS']).upper()

    options = []
    keys = ['A', 'B', 'C', 'D']

    if type == 'MCQ':
        for i in keys:
            options.append(input(f'Set options\n{i} > ').upper())
        answer = input3_str_answ_abcd.correctinput('Correct Answer\n' ,['A','B','C','D']).upper()
        Q_options = dict(zip(keys, options))
        Q_x[f'Question{Q_no}'] = question
        Q_x['Type'] = type
        Q_x['Options'] = Q_options
        Q_x['Answer'] = answer

    elif type == 'FILL_BLANKS':
        answer = input('Correct Answer "____"\n').upper()
        Q_x[f'Question{Q_no}'] = question
        Q_x[f'Type'] = type
        Q_x['Answer'] = answer

    elif type == 'T-F':
        answer = input3_str_answ_tf.correctinput('Correct Answer\n' , ['T','F']).upper()
        option = {
            'A': 'T',
            'B': 'F'
        }
        Q_x[f'Question{Q_no}'] = question
        Q_x['Type'] = type
        Q_x['Options'] = option
        Q_x['Answer'] = answer

    return Q_x

while Q_no < How_many_Q:
    Q_no += 1
    data_as_dict = data_input()
    Question_dict[f'Q.{Q_no}'] = data_as_dict

# File name input:
file_name = input('Save file as: ')
# Save Dict as txt file:
save_Q_data_input.save_as_file(Question_dict , file_name)

os.system('cls')