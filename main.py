import sys
import os 

name_string = "$name"
dir_path = os.path.dirname(os.path.realpath(__file__))
cwd = os.getcwd()
template_dir = os.path.join(dir_path, "templates")
input_name = sys.argv[1]
