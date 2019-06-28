*** Settings ***
Library           Selenium2Library
Library           RequestsLibrary
Library           DatabaseLibrary

*** Test Cases ***
interface
    [Documentation]    接口测试demo
    [Setup]
    Create Session    baidu    http://www.baidu.com
    ${resp}=    Get Request    baidu    /
    Should Be Equal As Strings    ${resp.status_code}    200
