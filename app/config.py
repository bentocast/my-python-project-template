from pydantic import BaseModel
import yaml

CONFIG_FILE_PATH = 'config/config.yaml'

class Config(BaseModel):
    key_1: str
    key_2: str

    @classmethod
    def from_file(cls):
        with open(CONFIG_FILE_PATH, 'r', encoding='utf-8') as file:
            raw_conf = yaml.safe_load(file)
        
        return cls(**raw_conf)
