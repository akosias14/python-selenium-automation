Feature: Color Selection Test
  Scenario: Verify color selection on a product page
    Given Open target product A-88345426 page
    When the user selects each color on the page
    Then the selected color should be verified
