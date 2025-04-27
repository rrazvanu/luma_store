from time import sleep

from behave import *


@when('Order Placement: I navigate to the home page')
def step_impl(context):
    context.base_page.navigate_to_home_page()


@when('Order Placement: I search for the product "{product_name}"')
def step_iml(context, product_name):
    context.order_placement_page.search_entire_store(product_name)


@when('Order Placement: I select the product "{product_name}"')
def step_impl(context, product_name):
    context.order_placement_page.select_product(product_name)


@when('Order Placement: I select the size "{size}"')
def step_impl(context, size):
    context.order_placement_page.select_size(size)


@when('Order Placement: I select the color "{color}"')
def step_impl(context, color):
    context.order_placement_page.select_color(color)


@when('Order Placement: I click the add to cart button')
def step_impl(context):
    context.order_placement_page.click_add_to_cart_button()
    sleep(3)


@when('Order Placement: I navigate to my cart')
def step_impl(context):
    context.base_page.navigate_to_my_cart()


@when('Order Placement: I click the checkout button')
def step_impl(context):
    context.order_placement_page.click_proceed_to_checkout_button()


@when('Order Placement: I click the NEXT button')
def step_impl(context):
    sleep(2)
    context.order_placement_page.click_checkout_next_button()


@when('Order Placement: I click the PLACE ORDER button')
def step_impl(context):
    sleep(2)
    context.order_placement_page.click_place_order_button()


@when('Order Placement: I validate the order is completed')
def step_impl(context):
    context.order_placement_page.validate_order_complete()


@when('Order Placement: I set the quantity to "{quantity}"')
def step_impl(context, quantity):
    context.order_placement_page.set_quantity(quantity)


@when('Order Placement: I verify the info message regarding the maximum quantity is displayed')
def step_impl(context):
    context.order_placement_page.validate_max_purchase_error_message()


@when('Order Placement: I verify the info message regarding the invalid quantity is displayed')
def step_impl(context):
    context.order_placement_page.validate_invalid_value_error_message()


@when('Order Placement: I verify the required field error message is displayed')
def step_impl(context):
    context.order_placement_page.validate_required_field_error_message()
