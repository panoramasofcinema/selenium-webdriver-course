from selenium import webdriver
import pytest


# @pytest.fixture(params=["chrome", "firefox", "safari"])
@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    # browser = request.param

    # Install and declare driver
    print(f'Creating {browser} driver')
    if browser == "chrome":
        my_driver = webdriver.Chrome()
    elif browser == 'firefox':
        my_driver = webdriver.Firefox()
    elif browser == 'safari':
        my_driver = webdriver.Safari()
    else:
        raise TypeError(
            f"Expected 'chrome', 'firefox', 'safari', but got {browser}")
    # my_driver.implicitly_wait(10)  # global time to wait before it fails

    yield my_driver
    print(f'Closing {browser} driver')
    my_driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser to execute test (chrome, firefox, safari)"
    )
