import sys
sys.path.insert(0, '/var/www/alexprime')

activate_this = '/root/.local/share/virtualenvs/alexprime-fBvwiSea/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file.read(), dict(__file__=activate_this))

from main import app as application