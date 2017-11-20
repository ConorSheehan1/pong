# Set up
(optional) create a virtual environment
```
conda create -n pong python=3
```
(required)
```
pip install -r requirements.txt
mv config.py.EXAMPLE config.py
```
you'll need to edit some values to get captchas and log in to work

# Run

```
python __init__.py
```
or if you've set up the pong virtual environment
```
. ./up.sh
```
go to localhost, default port is 5000  
check the output of your shell as it may be different
