import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
import datetime
driver = None

dateTime = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser = request.config.getoption("browser")
    if browser == "chrome":
        chr_option = Options()
        chr_option.add_experimental_option("detach", True)
        # service = ChromeService(
        #     executable_path=r"D:\Python_Program-master\Python_Program-master\drivers\chromedriver.exe")
        driver = webdriver.Chrome(options=chr_option)
        # driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()

    else:
        driver = webdriver.Edge()

    driver.implicitly_wait(10)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
        """
            Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
            :param item:
            """
        pytest_html = item.config.pluginmanager.getplugin('html')
        outcome = yield
        report = outcome.get_result()
        extra = getattr(report, 'extra', [])

        if report.when == 'call' or report.when == "setup":
            xfail = hasattr(report, 'wasxfail')
            if (report.skipped and xfail) or (report.failed and not xfail):
                file_name = report.nodeid.replace("::", f"_{dateTime}") + ".png"
                _capture_screenshot(file_name)
                if file_name:
                    html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                         'onclick="window.open(this.src)" align="right"/></div>' % file_name
                    extra.append(pytest_html.extras.html(html))
            report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)

