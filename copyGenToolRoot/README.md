# Simple CLI python project
## Usage details later 

1. ### Create a new virtual environment
python3 -m pip -m venv mycopyvenv

2. ### Activate environment
source ./mycopyvenv/bin/activate

3. ### Download requirements under requirements.txt file
python3 pip -r install requirements.txt

4. ### Optional convert the project to an executable using uv
python3 pip install -e .

5. ### Run the program.
copygentool --path <path-to-the-folder> --verbose <print-logging-information> --dry-run <Used to display the sample of files to create>