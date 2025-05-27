Feature: Product Service

  Scenario: Read a single product by ID
    Given the following products
      | name    | category | price  | available |
      | Printer | Office   | 1200000| true      |
    When I visit the endpoint "/products/1"
    Then the response status code should be 200
    And the response should contain "Printer"

