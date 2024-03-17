Feature: API Tests

  Scenario: Validate Pet Schema
    When I send a GET request to "/pets/1"
    Then the response status code should be 200
    And the response body should match the pet schema

  Scenario Outline: Find Pets by Status
    When I send a GET request to "/pets/findByStatus" with the status "<status>"
    Then the response status code should be 200
    And each pet in the response has valid properties for the status "<status>"
  
    Examples:
      | status    |
      | available |
      | pending   |
      | sold      |

  Scenario Outline: Get Pet by ID
    When I send a GET request to "/pets/<invalid_id>"
    Then the response status code should be 404
