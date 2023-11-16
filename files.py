import os

open_file = open("Created.txt","r+")
# open_file.write("File created.\nDone\n")
Readed_lines = open_file.read(6)
print(Readed_lines)
print(open_file.tell())
reposition = open_file.seek(0,0)
print(reposition)
print(open_file.tell())
open_file.close()

# os.mkdir('Done')
print(os.getcwd)