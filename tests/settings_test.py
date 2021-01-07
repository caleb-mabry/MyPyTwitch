import pytest
from bot.settings import Settings

def test_settings_file_raises_filenotfound_if_not_exist():
    config = Settings()
    config.FILENAME = 'FAKEFILENAME.JPG'
    with pytest.raises(FileNotFoundError):
        config._read_settings_file()

def test_if_settings_file_returns_dict():
    assert type(Settings()._read_settings_file()) == dict
