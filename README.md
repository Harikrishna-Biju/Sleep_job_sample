# chef-integration-tests
repo for pyTest and manual tests against all products for use in the Integration and Staging/QA environments

Home page for integration testing - https://chefio.atlassian.net/wiki/spaces/AR/pages/3014066189/Running+tests+and+filing+bug+reports

## Setting up your workstation
- install python - https://www.python.org/downloads/
- install pytest - https://docs.pytest.org/en/stable/getting-started.html
- install junitparser - `pip install junitparser`
- install pipx - https://pipx.pypa.io/stable/installation/#on-windows
- install poetry - https://python-poetry.org/docs/
- (generate poetry scaffold for new project)

## Running the repo locally

## Running the Github Actions

## Qmetry integration
API key - 6b328012ae5e9d7aacaae43aae5059c3719168ea2b3731a3ecdd6261c92b8ecec05bd2c0f88dee46be821f0eb0590d1fbb9d22b9f78f561658a90b0d0a0a96ca809876e7976f1a511a6b164095ffadea 




## Folder structure
- `/bin` contains copies of the three chef360 command lines

## To-do
1. Folders for core functions and 5 initial test cases
CHEF-TC-723 - Bulk Enrolment - https://progresssoftware.atlassian.net/plugins/servlet/ac/com.infostretch.QmetryTestManager/qtm4j-test-management?project.key=CHEF&project.id=11060#!/TestCaseDetail/w9YINzbuGYY8x/1?projectId=11060
CHEF-TC-729 -  Node Enrolment providing WinRM credentials - https://progresssoftware.atlassian.net/plugins/servlet/ac/com.infostretch.QmetryTestManager/qtm4j-test-management?project.key=CHEF&project.id=11060#!/TestCaseDetail/dgDcqD6fdDD51/1?projectId=11060
CHEF-TC-178 - Enrollment level after manually calling register node CLI/API.
CHEF-TC-175 - Enroll one linux node using ssh key
CHEF-TC-174 - Install a skill without any pre-defined roles
1. Add Irfan's Poetry library - https://progresssoftware-my.sharepoint.com/personal/isyed_progress_com/_layouts/15/stream.aspx?id=%2Fpersonal%2Fisyed%5Fprogress%5Fcom%2FDocuments%2FRecordings%2FMeeting%20with%20Irfan%20Syed%2D20241025%5F194347%2DMeeting%20Recording%2Emp4&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0&ct=1730076495236&or=OWA%2DNT%2DMail&cid=d8b2f42c%2Db4dc%2Def70%2D1011%2D99f71b5915ea&ga=1&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2E959c7c6c%2De949%2D455b%2D9e98%2De0cd8b72725c 
1. Automate pulling the latest command lines at GHA time from 
    - https://github.com/progress-platform-services/chef-node-management-cli/releases 
    - https://github.com/progress-platform-services/chef-courier-cli/releases
    - https://github.com/progress-platform-services/chef-platform-auth-cli/releases
1. Get Windows & MacOS versions of CLIs (make switchable)


## Setup and run the tests with poetry

1. Navigate to the Home directory

   ```sh
   cd chef-integration-tests
   ```
2. If any python environment is already set then delete it
   
   ```sh
   deactivate
   ```

3. Install poetry

   ```sh
   export PYTHONPATH=$(pwd)
   poetry config virtualenvs.in-project true
   poetry install --no-ansi --no-root

   source .venv/bin/activate
   ```

   Installing the .venv in the current directory is important and makes management of the virtual environments across the projects easier.

4. Run the tests

   ```sh
   pytest integration-tests/sample-test --junitxml=reports/report.xml
   ```

