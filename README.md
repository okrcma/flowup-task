# apitimer

## Install

1. Get Python 3.10
2. (Optional) Create virtual environment to not clutter your global one
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install requirements
   ```bash
   python3 -m pip install -r requirements.txt
   ```
4. Add sources to PYTHONPATH
   ```bash
   export PYTHONPATH=$(pwd):$PYTHONPATH
   ```

## Run

```bash
python3 apitimer/app.py
```

And open http://127.0.0.1:8000/docs.
