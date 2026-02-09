This is a playwright test project 
# PowerShell commands to activate virtual environment

Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process

.\play_env\Scripts\Activate.ps1

# Command to install dependencies
pip install -r requirements.txt
# Command to run tests
pytest
# Command to generate HTML report
pytest --html=report.html
# Command to open HTML report
playwright show-report
# To run tests in headed mode with chromium browser by default, the following options are added in pytest.ini
;    --headed
;    --browser=chromium
