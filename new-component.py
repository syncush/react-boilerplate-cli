import sys
import os 

name_string = "$componentName"
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

def create_file(template_file_path, new_file_name, spaces):
    new_file = open(os.path.join(component_dir, new_file_name), "w+")
    template_file = open(template_file_path, "r")

    template_string = template_file.read().replace("    ", spaces)
    new_file_string = template_string.replace(name_string, input_name)
    new_file.write(new_file_string)

    new_file.close()
    template_file.close()

args_set = set(sys.argv)

spaces = "    "
if "--2spaces" in args_set:
    spaces = "  "

create_file(os.path.join(template_dir, "index.js.template"), "index.js", spaces)
create_file(os.path.join(template_dir, "style.css.template"), input_name + ".css", spaces)

component_template_name = "class"
if "--hooks" in args_set:
    component_template_name = "hooks"
elif "--func" in args_set or "--function" in args_set:
    component_template_name = "func"

template_file_path = os.path.join(components_dir,
                        component_template_name + ".template")
create_file(template_file_path, input_name + ".jsx", spaces)
