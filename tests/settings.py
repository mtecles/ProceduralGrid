import os
from glob import glob

# Load test ENV VARS
for env_var in glob(os.path.join('tests', 'env', '*')):
    with open(env_var, 'r') as env_var_file:
        os.environ.setdefault(os.path.basename(env_var), env_var_file.read().strip())

# Path shortcuts
PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
PROJECT_NAME = os.path.basename(PROJECT_ROOT)
PROJECT_PATH = lambda *a: os.path.join(PROJECT_ROOT, *a)


SIZE = {
    'LAYOUT': {'W': 100, 'H': 100},
    'CELL': {'W': 10, 'H': 10},
    'MIN_ROOM_CELLS': 4,
    'MAX_ROOM_CELLS': 20,
}
