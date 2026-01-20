import json
import os
import re

VSCODE_SETTINGS_FILE = '.vscode/settings.json'
REQUIREMENTS_FILE = 'requirements.in'

def extract_package_names(requirements_file):
    package_names = []
    if not os.path.exists(requirements_file):
        return package_names
    
    with open(requirements_file, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            package_name = re.split(r'[<>=!]', line)[0].strip()
            if package_name:
                package_names.append(package_name)
    
    return package_names

def generate_vscode_paths(package_names):
    paths = []
    for package in package_names:
        normalized_package = package.replace('-', '_')
        path = f"./bazel-bazel-python-boilerplate/bazel-out/darwin_arm64-fastbuild/bin/src/package/main.runfiles/rules_python++pip+pip_311_{normalized_package}/site-packages"
        paths.append(path)
    return paths

def update_vscode_settings(extra_paths):
    os.makedirs('.vscode', exist_ok=True)
    settings = {}
    if os.path.exists(VSCODE_SETTINGS_FILE):
        try:
            with open(VSCODE_SETTINGS_FILE, 'r') as f:
                settings = json.load(f)
        except json.JSONDecodeError:
            print(f"Warning: Could not parse existing {VSCODE_SETTINGS_FILE}, creating new one")
            settings = {}
    
    settings["python.analysis.extraPaths"] = extra_paths
    
    if "python-envs.defaultEnvManager" not in settings:
        settings["python-envs.defaultEnvManager"] = "ms-python.python:system"
    
    if "python-envs.pythonProjects" not in settings:
        settings["python-envs.pythonProjects"] = []
    
    with open(VSCODE_SETTINGS_FILE, 'w') as f:
        json.dump(settings, f, indent=4)
    
def main():    
    packages = extract_package_names(REQUIREMENTS_FILE)    
    extra_paths = generate_vscode_paths(packages)
    update_vscode_settings(extra_paths)
    

if __name__ == '__main__':
    main()