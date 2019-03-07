import sys
import os 

name_string = "$componentName"
styles_extention_token = "$styleExtention"
dir_path = os.path.dirname(os.path.realpath(__file__))
template_dir = os.path.join(dir_path, "templates")
components_dir = os.path.join(template_dir, "components")

cwd = os.getcwd()
input_name = sys.argv[-1]
component_dir = os.path.join(cwd, input_name)

if os.path.exists(component_dir):
    print("Component already exists")
    exit()

os.makedirs(component_dir)

def create_file(template_file_path, new_file_name, spaces, styleExtention="css"):
    new_file = open(os.path.join(component_dir, new_file_name), "w+")
    template_file = open(template_file_path, "r")

    template_string = template_file.read().replace("    ", spaces)
    new_file_string = template_string.replace(name_string, input_name)
    new_file_string = new_file_string.replace(styles_extention_token, styleExtention)
    new_file.write(new_file_string)

    new_file.close()
    template_file.close()

args_set = set(sys.argv)

spaces = "    "
if "--2spaces" in args_set:
    spaces = " " * 2

styles_extention = 'css'
if '--sass' in args_set:
    styles_extention = 'scss'
if '--less' in args_set:
    styles_extention = 'less'

react_file_extention = 'jsx'
index_file_extention = 'js'
if '--ts' in args_set:
    react_file_extention = 'tsx'
    index_file_extention = 'ts'

create_file(os.path.join(template_dir, "index.js.template"), "index." + index_file_extention, spaces)
create_file(os.path.join(template_dir, "style.css.template"), input_name + '.' + styles_extention, spaces, styles_extention)

component_template_name = "class"
if "--hooks" in args_set:
    component_template_name = "hooks"
elif "--func" in args_set or "--function" in args_set:
    component_template_name = "func"
elif "--ts" in args_set:
    component_template_name = "ts_class"

template_file_path = os.path.join(components_dir,
                        component_template_name + ".template")
create_file(template_file_path, input_name + '.' + react_file_extention, spaces, styles_extention)

if "--story" in args_set:
    story_file_path = os.path.join(template_dir, "stories.js.template")
    create_file(story_file_path, 'stories.' + index_file_extention, spaces)
