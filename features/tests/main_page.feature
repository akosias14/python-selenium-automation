Feature: Verify empty cart message on target.com

  Scenario: User opens target.com and checks empty cart message
    Given open target webpage "url"
    When the user clicks on the Cart icon
    Then verify that the user see the message Your cart is empty
