import yaml

class ConfigManager:
    def __init__(self, path: str = "src/configs/settings.yaml"):
        try:
            with open(path, "r") as f:
                self.config = yaml.safe_load(f) or {}
        except:
            self.config = {}

    def get(self, key: str, default=None):
        return self.config.get(key, default)