# Created by ms.kerry at 11/11/23
Feature: Verify Sign In functionality on target.com for logged out users

  Scenario: Access Sign In as a logged out user
    Given open target main page
    When  clicks on the Sign In button
    And From right side navigation menu, click Sign In
    Then verify that the email field is present

