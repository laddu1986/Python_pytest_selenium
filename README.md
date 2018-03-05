# Test Assignment for Senior QA Engineer Position

## Overview
Test assignment consists of a simple test automation project. [Zendesk](https://www.zendesk.com/) was selected as an application under test based on this two lists:
- [Sites Using React]https://github.com/facebook/react/wiki/Sites-Using-React
- [Top 32 Sites Built With ReactJS](https://medium.com/@coderacademy/32-sites-built-with-reactjs-172e3a4bed81)

## Implementation Details

The following instruments were used to accomplish automation part:
- *Python 3.6.1*
- *pytest 3.4.1*
- *Selenium 3.9.0*

The following tests were covered by automation scripts:
- verify that chat plan prices on [chat prices](https://www.zendesk.com/chat/compare/#compare) page correspond to expected values

Please note that the main reason of the automation assignment is to demonstrate the ability to automate tests, code styling, approach, architectural solution, etc.

## Requirements
In order to run the tests you need to have the below requirements to be satisfied:
- latest *Python 3* (can be downloaded from official Python [website](https://www.python.org/)); make sure *Python* is added to environemnt variables
- latest *pytest* (can be install in terminal with *Python* package manager *pip*: `pip install pytest`); make sure *pytest* is added to environemnt variables
- latest *Selenium* (can be install in terminal with *Python* package manager *pip*: `pip install selenium`)

Tools needed to run the tests are also specified in **requirements.txt** file. Once *Python* is installed you can install other tools by running in terminal `pip -r PATH_TO_PROJECT_FOLDER/requirements.txt`.

In order for tests to launch browsers you need to have corresponding **drivers** available on your machine (can be downloaded from Selenium [download page](http://www.seleniumhq.org/download/)). Make sure the path where drivers are located is added to environemnt variables. In presented solution the following browsers are supported: *Chrome*, *Firefox*, *Safari* and  *Internet Explorer*.

## Tests Execution
To execute tests run the following command in terminal:
- `pytest PATH_TO_PROJECT_FOLDER/test`
Another way to execute test is running in terminal:
- `python -m pytest PATH_TO_PROJECT_FOLDER/test`

The following **custom options** for test launch are supported:
- *--browser* which is used to specify browser for tests to run in; supported values: *chrome*, *firefox*, *safari*, *ie*; *chrome* is default option; for example, to run tests in *firefox* run in terminal `pytest --browser=firefox PATH_TO_PROJECT_FOLDER/test`
- *--config* which is used to specify config file; takes path to config file as an input; by default *config.json* file located in project root folder is used