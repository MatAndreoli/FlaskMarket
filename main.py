import os
from pathlib import Path

from dotenv import load_dotenv, dotenv_values

from src import app

dotenv_path = Path('src/.env')
load_dotenv(dotenv_path=dotenv_path)
all_envs = dotenv_values(dotenv_path=dotenv_path)

print(all_envs['BOTH'])
port = os.getenv('PORT')
host = os.getenv('HOST')

if __name__ == '__main__':
    app.run(host=host, port=port, debug=True)
