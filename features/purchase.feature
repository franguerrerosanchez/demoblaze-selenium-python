Feature: Purchase Process for Samsung Galaxy S6 on Demoblaze

  Scenario: Add Samsung Galaxy S6 to Cart
    Given I am on the demoblaze.com homepage
    When I view the "Samsung Galaxy S6" details
    And I add the product to the cart
    And I navigate to the cart
    Then I should see the product "Samsung Galaxy S6" in the cart
    And I should see exactly 1 unit of the product "Samsung Galaxy S6" in the cart
    And I close the browser
