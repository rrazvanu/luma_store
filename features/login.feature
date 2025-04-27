Feature: Login feature

  @smoke @regression @login @login_success
  Scenario: Login - Successful authentication
    Given Login: I navigate to login page
    When Login: I complete valid credentials
    Then Login: I validate the successful login for "Razvan Iancu"
    Then Login: I log out
    # In this test we can observe a bug, the welcome message is not displayed after log in