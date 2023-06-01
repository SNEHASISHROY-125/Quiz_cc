
import shutil

def txt_encoder(save_name):
    '''DICT to TXT Encoder , Output as txt.'''
    # Specify the paths and names of the original file and the copy
    original_file = file_name
    destination_directory = Path            #"C:\Users\Snehasish\Documents\Quiz_game\questions"
    copy_file = save_name+".txt"

    # Construct the full path of the copy file in the destination directory
    copy_file_path = f"{destination_directory}/{copy_file}"

    # Copy the contents of the original file to the copy file in the destination directory
    shutil.copyfile(original_file, copy_file_path)

'''*************************************[FUNCTIONS]**********************************************'''
# Empty file txt:
file_name = 'Empty_file_txt'
# File path to save files:
Path = r"C:\Users\Snehasish\Documents\Quiz_game\questions"

def save_as_file(Q , n):
    append_Q = open(file_name , 'a')
    append_Q.write(f'{Q}\n')
    append_Q.close()

    txt_encoder(n)                         # Above two attributes will be passed to this function
    wipe_all = open(file_name, 'w')  # After saving the file , parent-> file gets wiped out.
    wipe_all.truncate(0)
    wipe_all.close()
        
