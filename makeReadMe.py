# remakes the readme file

import os

DIR = os.path.dirname(os.path.abspath(__file__))

output = []

for  file in os.listdir(DIR):
    if file.endswith('.md') and file != 'ReadMe.md':
        print(file)
        output.append('[{0}]({0})  \n'.format(file))
    
    
with open(os.path.join(DIR, 'ReadMe.md'),'w') as f:
    f.writelines(output)

