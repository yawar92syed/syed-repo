from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from configuration import ConfigForm
def before_all(context):
  pass


def before_feature(context, feature):
    # Executed before each feature is run
    pass


def before_scenario(context, scenario):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


def after_scenario(context, scenario):
    # Close the browser after each scenario
    context.driver.quit()
    pass

def after_step(context, step):
    pass


def after_feature(context, feature):
    # Executed after each feature is run
    pass


def after_all(context):
    # Executed once after all scenarios are run
    pass

