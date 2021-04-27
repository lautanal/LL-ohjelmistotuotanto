*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Main Page

*** Test Cases ***
Register With Valid Username And Password
    Go To Register Page
    Set Username  lasse
    Set Password  lasse123
    Set Password Confirmation  lasse123
    Submit Register
    Register Should Succeed

Register With Too Short Username
    Go To Register Page
    Set Username  ka
    Set Password  kalle456
    Set Password Confirmation  kalle456
    Submit Register
    Register Page Should Be Open
    Page Should Contain  Too short or nonalphabet username

Register With Too Short Password
    Go To Register Page
    Set Username  kari
    Set Password  kari123
    Set Password Confirmation  kari123
    Submit Register
    Register Page Should Be Open
    Page Should Contain  Too short password

Register With Passwords Do Not Match
    Go To Register Page
    Set Username  kari
    Set Password  kari1234
    Set Password Confirmation  kari12345
    Submit Register
    Register Page Should Be Open
    Page Should Contain  Passwords do not match

Succesful Register And Login Thereafter
    Go To Register Page
    Set Username  lasse
    Set Password  lasse123
    Set Password Confirmation  lasse123
    Submit Register
    Go To Login Page
    Set Username  lasse
    Set Password  lasse123
    Submit Credentials
    Login Should Succeed

Failed Registration And Login Thereafter
    Go To Register Page
    Set Username  seppo
    Set Password  seppo123
    Set Password Confirmation  seppo1234
    Submit Register
    Go To Login Page
    Set Username  seppo
    Set Password  seppo123
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Login Should Succeed
    Main Page Should Be Open

Register Should Succeed
    Welcome Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Login

Submit Register
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

