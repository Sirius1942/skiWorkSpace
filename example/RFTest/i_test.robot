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

testTemplate
    [Tags]    templa
    [Template]    hello
    张三    我是张三
    李四    我是李四
    王五    我有大刀

kw_login
    [Tags]    ukw_login
    login    chenjiusi    123456

kw_login_worngpassword
    [Tags]    ukw_login
    login    chenjiusi    12345999

testdb
    Get_database
    ${a}    Query    select * from persons

*** Keywords ***
login
    [Arguments]    ${username}    ${password}
    Open Browser    http://localhost:9527    chrome
    input text    name=username    ${username}
    input text    name=password    ${password}
    click button    id=login_button
    Close Browser

hello
    [Arguments]    ${name}    ${message}
    log    hello ${name},receive ${message}
    Should Be Equal As Strings     ${message}    我有大刀

Get_database
    [Timeout]
    Connect To Database Using Custom Params    sqlite3    "D:/code/autotest/testtwo/testThree/p/testdb.db3"
