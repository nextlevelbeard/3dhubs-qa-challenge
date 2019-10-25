@manufacture
Feature: Manufacture
  As a user
  I want to be easily to get quotes on manufacturing from 3D files
  so I can better plan my budget

  Background:
    Given I go to 3D Hubs
    And I choose to get a quote

  @upload
  Scenario: Can proceed to checkout after uploading a 3D model file
    Given I upload a file
    And I enter my email
    When I press Continue
    And I login
    Then I should see the checkout

  @sample
  Scenario: Can proceed to checkout by using the sample
    Given I choose to upload a sample part
    And I enter my email
    When I press Continue
    And I login
    Then I should see the checkout