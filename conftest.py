import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help='Choose language: ')


@pytest.fixture(scope='function')
def browser(request):
    browser_lang = request.config.getoption('language')
    if browser_lang:
        print('\nstart chrome browser for test..')
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': browser_lang})
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    else:
        raise pytest.UsageError('please add language')
    yield browser
    print('\nquit browser..')
    browser.quit()
