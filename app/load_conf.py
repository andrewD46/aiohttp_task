import os
import yaml


def load_config():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    config_file = base_dir + '/config.yaml'
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
    return config
