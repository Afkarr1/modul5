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

  Scenario: List all products
    Given the following products
      | name    | category | price  | available |
      | Printer | Office   | 1200000| true      |
      | Scanner | Office   | 900000 | true      |
    When I visit the endpoint "/products"
    Then the response status code should be 200
    And the response should contain "Printer"
    And the response should contain "Scanner"

  Scenario: Search for products by category
    Given the following products
      | name    | category | price  | available |
      | Printer | Office   | 1200000| true      |
      | Fan     | Home     | 350000 | true      |
    When I visit the endpoint "/products?category=Office"
    Then the response status code should be 200
    And the response should contain "Printer"
    And the response should not contain "Fan"
