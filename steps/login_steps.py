import logging
from behave import *
import config


def catch_exceptions(step_func):
    def wrapper(*args, **kwargs):
        try:
            return step_func(*args, **kwargs)
        except Exception as e:
            logging.error(f"Caught exception: {e}")

    return wrapper


@given('Login: I navigate to login page')
def step_impl(context):
    context.login_page.navigate_to_login_in_page()


@when('Login: I complete valid credentials')
@catch_exceptions
def step_iml(context):
    context.login_page.set_email(config.email)
    context.login_page.set_password(config.user_password)
    context.login_page.click_sign_in_button()


@then('Login: I validate the successful login for "{user_name}"')
def step_impl(context, user_name):
    context.login_page.validate_login(user_name)


@then('Login: I log out')
def step_impl(context):
    context.login_page.log_out()
