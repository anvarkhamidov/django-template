
import sys
import os
import json
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class Config:

    __config = {
        'secret_key': str(os.getenv('SECRET_KEY')),
        'mode': str(os.getenv('MODE')),
        'site_uri': str(os.getenv('SITE_URI')) or 'localhost',
        'psql_host': str(os.getenv('PSQL_HOST')),
        'psql_name': str(os.getenv('PSQL_NAME')),
        'psql_user': str(os.getenv('PSQL_USER')),
        'psql_password': str(os.getenv('PSQL_PASSWORD')),
        'sqlite_name': str(os.getenv('SQLITE_NAME'))
    }

    __mode = ['dev', 'prod']

    @staticmethod
    def get(key):
        try:
            return Config.__config[key]
        except:
            raise KeyError(f"Key `{key}` does not exist in config")
    
    @staticmethod
    def validate():
        empty_vars = []
        if Config.get('mode') not in Config.__mode:
            raise NameError('ERROR: Mode is set incorrect. Available options are: `dev` and `prod`')
        
        for key, value in Config.__config.items():
            if Config.get('mode') == 'dev' and key.startswith('psql_'):
                continue
            
            elif Config.get('mode') == 'prod' and key.startswith('sqlite_'):
                continue

            if not value:
                empty_vars.append(key)

        if empty_vars:
            raise NameError(f'ERROR: Variables {", ".join(empty_vars)} are empty.')

