from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from configuration import ConfigForm
from methods.utilities import assert_element_exists


@when(u'the user enters valid credentials')
def step_impl(context):
    assert_element_exists(context.driver, By.XPATH"")

@when(u'clicks the login button')
def step_impl(context):
    pass


@then(u'the user should be redirected to the form page')
def step_impl(context):
    pass