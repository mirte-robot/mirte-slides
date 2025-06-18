# mirte-slides

# Lite:

## Windows:
```bash
cmd # switch to cmd, powershell doesn't work with the .bat version
cd lite
python3 -m venv docs_env                             
docs_env\Scripts\activate.bat
pip install -r requirements.txt
playwright install # (optional with --with-deps)
make revealjs
```

## Linux
```bash
cd lite
python3 -m venv docs_env                             
source docs_env/bin/activate
pip install -r requirements.txt
playwright install # (optional with --with-deps)

make revealjs # output will be in _build/revealjs
# if you have nodejs installed and want live reload on changes
npx nodemon -w ./ -i _build -e rst,scss -x "make revealjs" 
```