*** Settings ***
Library           Selenium2Library

*** Test Cases ***
selenium demo
    [Documentation]    test_login
    [Tags]    selenium
    [Template]
    Open Browser    http://www.baidu.com    chrome
    input text    id=kw    test_robot
    click button  id=su
