import json

from pathlib import Path
from typing import Dict, Any

from .variablemappings.settingsFields import SettingsFields


class Settings:
    def __init__(self):
        self.FILENAME = 'settings.json'
        self.settings = self._read_settings_file()

    def _read_settings_file(self) -> Dict[SettingsFields, Any]:
        if Path(self.FILENAME).exists():
            with open('settings.json') as file:
                return json.load(file)
        else:
            raise FileNotFoundError(f'{self.FILENAME} does not exist')
