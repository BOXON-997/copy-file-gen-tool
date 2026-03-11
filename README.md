# copy-file-gen-tool

# Simple CLI python project
## Usage details later 

1. ### Create a new virtual environment
python3 -m venv mycopyvenv

2. ### Activate environment
source ./mycopyvenv/bin/activate

3. ### Download requirements under requirements.txt file
python3 -m pip -r install requirements.txt

4. ### Optional convert the project to an executable using uv
python3 -m pip install -e .

5. ### Run the program.
copygentool --path <path-to-the-folder> --verbose <optional-for-logging-information-on-screen> --dry-run <Displays-a-list-of-files-to-be-created-omit-to-create-file-copies>
Alternatively you can run only the cli.py file as so 

cd into project root on shell then run
### >>> cd ./copyGenToolRoot/
### >>> python3 -m copyGenTool.cli --path <path-to-the-folder> --verbose <optional-for-logging-information> --dry-run <Displays-a-log-of-files-to-be-created-omit-to-create-file-copies>

