Feature: Product Service

  Scenario: Read a single product by ID
    Given the following products
      | name    | category | price  | available |
      | Printer | Office   | 1200000| true      |
    When I visit the endpoint "/products/1"
    Then the response status code should be 200
    And the response should contain "Printer"

  Scenario: Update a product
    Given the following products
      | name    | category | price  | available |
      | Printer | Office   | 1200000| true      |
    When I visit the endpoint "/products/1"
    Then the response status code should be 200
    When I update the product with the following data
      | name            | category | price   | available |
      | LaserJet Printer| Office   | 1400000 | true      |
    Then the response status code should be 200
    And the response should contain "LaserJet Printer"

  Scenario: Delete a product
    Given the following products
      | name    | category | price  | available |
      | Printer | Office   | 1200000| true      |
    When I delete the product with ID "1"
    Then the response status code should be 204

