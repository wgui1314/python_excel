import os
import yaml
class LoadConfig():
    def __init__(self):
        self.yml_path = os.path.join("config/external.yml")
        self.read()

    def read(self):

        # open方法打开直接读出来
        f = open(self.yml_path, 'r', encoding='utf-8')
        cfg = f.read()

        return yaml.load(cfg, Loader=yaml.SafeLoader)
    @classmethod
    def get_value(cls,name):
        return LoadConfig().read()[name]
    