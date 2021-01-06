import json

from typing import Dict, Any

from enumerations.settingsFields import SettingsFields


class Settings:
    def __init__(self):
        self.settings = self._read_settings_file()

    @staticmethod
    def _read_settings_file() -> Dict[SettingsFields, Any]:
        with open('settings.json') as file:
            return json.load(file)
