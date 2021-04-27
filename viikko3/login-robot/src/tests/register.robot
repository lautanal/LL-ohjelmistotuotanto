*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Create User  kalle  kalle123
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

*** Test Cases ***
Register With Already Taken Username And Valid Password
    Create User  kalle  kalle123
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

*** Test Cases ***
Register With Too Short Username
    Input Credentials  ka3  kalle123
    Output Should Contain  Too short or nonalphabet username

*** Test Cases ***
Register With Too Short Password
    Input Credentials  kalle  kalle
    Output Should Contain  Too short password

*** Keywords ***
Create User And Input New Command
    Input New Command
