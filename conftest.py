import pytest
import json
import os.path
from helpers.fixture import Application


fixture = None
config = None


# helper function to load config data from config file
def load_conf_file(file):
    global config
    if config is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            config = json.load(f)
    return config


# fixture setUp
@pytest.fixture
def app(request):
    global fixture
    parameters = load_conf_file(request.config.getoption('--config'))
    if fixture is None:
        fixture = Application(browser=request.config.getoption('--browser'),
                              pub_url=parameters['public_site']['root_url'],
                              priv_url=parameters['private_url']['root_url'],
                              user=parameters['private_url']['username'],
                              password=parameters['private_url']['password'])
        fixture.wd.get(fixture.pub_url)
        request.addfinalizer(fixture.destroy)
    return fixture


# test launch parameters
def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome')
    parser.addoption('--config', action='store', default='config.json')
