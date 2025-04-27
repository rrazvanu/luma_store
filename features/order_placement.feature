Feature: Order Placement feature

  @smoke @regression @order_placement @order_placement_success
  Scenario: Order Placement : Order Placement success
    Given Login: I navigate to login page
    When Login: I complete valid credentials
    When Order Placement: I navigate to the home page
    When Order Placement: I search for the product "Electra Bra Top"
    When Order Placement: I select the product "Electra Bra Top"
    When Order Placement: I select the size "M"
    When Order Placement: I select the color "Black"
    When Order Placement: I click the add to cart button
    When Order Placement: I navigate to my cart
    When Order Placement: I click the checkout button
    When Order Placement: I click the NEXT button
    When Order Placement: I click the PLACE ORDER button
    When Order Placement: I validate the order is completed
    Then Login: I log out


  @smoke @regression @order_placement @order_placement_invalid_quantity_0
  Scenario: Order Placement : An invalid quantity is provided
    Given Login: I navigate to login page
    When Login: I complete valid credentials
    When Order Placement: I navigate to the home page
    When Order Placement: I search for the product "Electra Bra Top"
    When Order Placement: I select the product "Electra Bra Top"
    When Order Placement: I select the size "M"
    When Order Placement: I select the color "Black"
    When Order Placement: I set the quantity to "0"
    When Order Placement: I click the add to cart button
    When Order Placement: I verify the info message regarding the invalid quantity is displayed
    Then Login: I log out


  @smoke @regression @order_placement @order_placement_max_quantity_error
  Scenario: Order Placement : The maximum quantity is exceeded
    Given Login: I navigate to login page
    When Login: I complete valid credentials
    When Order Placement: I navigate to the home page
    When Order Placement: I search for the product "Electra Bra Top"
    When Order Placement: I select the product "Electra Bra Top"
    When Order Placement: I select the size "M"
    When Order Placement: I select the color "Black"
    When Order Placement: I set the quantity to "10001"
    When Order Placement: I click the add to cart button
    When Order Placement: I verify the info message regarding the maximum quantity is displayed
    Then Login: I log out


  @smoke @regression @order_placement @order_placement_color_not_selected
  Scenario: Order Placement : Order Placement success
    Given Login: I navigate to login page
    When Login: I complete valid credentials
    When Order Placement: I navigate to the home page
    When Order Placement: I search for the product "Electra Bra Top"
    When Order Placement: I select the product "Electra Bra Top"
    When Order Placement: I select the size "M"
    When Order Placement: I click the add to cart button
    When Order Placement: I verify the required field error message is displayed
    Then Login: I log out


      @smoke @regression @order_placement @order_placement_size_not_selected
  Scenario: Order Placement : Order Placement success
    Given Login: I navigate to login page
    When Login: I complete valid credentials
    When Order Placement: I navigate to the home page
    When Order Placement: I search for the product "Electra Bra Top"
    When Order Placement: I select the product "Electra Bra Top"
    When Order Placement: I select the color "Black"
    When Order Placement: I click the add to cart button
    When Order Placement: I verify the required field error message is displayed
    Then Login: I log out