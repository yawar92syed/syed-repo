import random
import os
import allure
import requests
from selenium.common.exceptions import NoSuchElementException
import configuration
import time
import json
from methods import *


def trigger_webhook(total_failures, failure_details):
    # Use the correct webhook URL from configuration
    teams_webhook_url = configuration.configuration_system.webhook_url
    payload = {
        "@type": "MessageCard",
        "@context": "",
        "summary": "Test Automation Failure",
        "title": "Failed Failed Failed!!!!",
        "sections": [{
            "activityTitle": "Test Automation Failure",
            "activitySubtitle": "Errors occurred during test execution",
            "activityImage": "",
            "facts": [{
                "name": "Total Failures",
                "value": f"{total_failures}"
            }] + [
                         {
                             "name": f"Failure {i + 1}",
                             "value": detail
                         } for i, detail in enumerate(failure_details)
                     ]
        }]
    }
    try:
        response = requests.post(teams_webhook_url, json=payload)
        response.raise_for_status()  # Raise exception for HTTP errors
    except Exception as e:
        print("Error triggering webhook:", e)


def assert_element_exists(driver, by, locator, failure_details):
    try:
        driver.find_element(by, locator)
    except NoSuchElementException:
        failure_details.append(f"Element not found: {locator}")
        total_failures = len(failure_details)
        trigger_webhook(total_failures, failure_details)
        raise AssertionError(f"Element not found: {locator}")