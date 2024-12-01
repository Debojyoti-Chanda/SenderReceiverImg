```bash
# Create a virtual environment
python -m venv myenv
# Activate the virtual environment (Linux/macOS)
source myenv/bin/activate
# Activate the virtual environment (Windows-CMD)
myenv\Scripts\activate.bat

pip3 freeze > requirements.txt

# Install the packages listed in the requirements.txt file
pip install -r requirements.txt
```

