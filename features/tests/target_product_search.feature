Feature: Add product to the cart and verify

  Scenario: Add a product to the cart and check the cart content
    Given open target page
    When search for a COAT
    Then add product to the cart
    Then Verify that the product is in the cart

    Scenario: verify that user can see product names and images
    Given open target page
    When search for Hats
    Then Verify that every product has a name and an image