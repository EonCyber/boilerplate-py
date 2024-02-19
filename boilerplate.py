import yaml
import sys
import os
import subprocess
import json
from jinja2 import FileSystemLoader, Environment

OUTPUT_PATH = 'output'
TEMPLATE_PATH = '../../templates'
CONFIG_PATH = 'config/base.yaml'

def open_config(path):
    with open(path) as f:
        data = f.read()
    return yaml.load(data, Loader=yaml.FullLoader)

def check_create_dir(path):
    arr = path.split("/")
    main_dir = arr[0]
    for folder in arr:
        if folder != main_dir:
            main_dir = main_dir + '/' + folder
        check_dir = os.path.isdir(main_dir)
        if not check_dir:
            os.mkdir(main_dir)
            print(main_dir, ' ===> Created')
    return main_dir

def modify_package_json():
    with open('package.json', 'r') as file:
        data = json.load(file)
    data['main'] = 'app.ts'
    data['description'] = 'Generated with Node-Scaffold.Py'
    data['scripts']['test'] = 'vitest'
    data['scripts']['start'] = 'tsx src/app.ts'
    data['scripts']['start:dev'] = 'tsx watch src/app.ts'
    data['scripts']['start:build'] = 'node dist/src/app.js'
    data['scripts']['build'] = 'tsup src'
    print(data)
    with open('package.json', 'w') as file:
        json.dump(data, file, indent=2)
    print('package.json ====> updated')
    
    
def generate_project(project_path):
    # check_create_output
    project_dir = check_create_dir(project_path)
    proj_init_comm = f"npm init -y"
    lib_install_comm = f"npm install express body-parser express-winston winston cors mongoose"
    dev_lib_install_comm = f"npm i -D typescript tsup tsx vitest @types/cors @types/express @types/cors"
    typescript_init_comm = f"npx tsc --init"
    #  change directory to output
    os.chdir(project_dir)
    # fire npm
    print(proj_init_comm, '===> Executing')
    subprocess.call(proj_init_comm, shell=True)
    print('package.json ===> Created')
    print(lib_install_comm, '===> Executing')
    subprocess.call(lib_install_comm, shell=True)
    print(dev_lib_install_comm, '===> Executing')
    subprocess.call(dev_lib_install_comm, shell=True)
    print(typescript_init_comm, '===> Executing')
    subprocess.call(typescript_init_comm, shell=True)
    print('tsconfig.json ===> Created')
    # Update Package.json
    modify_package_json()
    os.chdir('../..')

def generate_project_structure(project_path, structure_arr):
    for path in structure_arr:
        check_create_dir(project_path + '/' + path)

def generate_components(project_path, comp_infos, templates_path):
    os.chdir(project_path)
    for key in comp_infos:
        config = comp_infos[key]
        template = open_template(templates_path, config['template'])
        render_template(template, {}, config['output'], config['fileName'])
    os.chdir('../..')

def open_template(template_dir, template_filename):
    loader = FileSystemLoader(template_dir)
    env = Environment(loader=loader)
    return env.get_template(template_filename)

def render_template(template, params, output_path, filename):
    final_path = '.' + output_path + '/' + filename
    template.stream(parameters=params).dump(final_path)
    print(final_path, '===> Created')

def bootstrap_project(project_path):
    os.chdir(project_path)
    start_command = "npm run start:dev"
    print(start_command, '===> Executing')
    subprocess.call(start_command, shell=True)
    
def main(project_name):
    project_path = OUTPUT_PATH + '/' + project_name
    # Create Node - Typescript Project with NPM
    generate_project(project_path)
    # Load Template Configuration of base.yaml
    configs = open_config(CONFIG_PATH)
    # Generate Project Folder Structure
    generate_project_structure(project_path, configs['structure'])
    # Generate Components
    generate_components(project_path, configs['components'], TEMPLATE_PATH)
    # Bootstrap Project
    bootstrap_project(project_path)
    
if __name__ == "__main__":
    project_name = sys.argv[1]
    main(project_name)