# Test Automation Framework

A simple test automation framework using Playwright and Python with pytest for testing web applications.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Install Playwright Browsers

```bash
playwright install
```

### 3. Configure Environment

Create a `.env` file in the project root and add your test credentials:

```
TEST_USERNAME=qa-ui-automation-external@abc.com
TEST_PASSWORD=abc123
```

### 4. Configure Test Settings

Edit `config/config.py` to customize:
- Browser type (chromium, firefox, webkit)
- Headless mode (True/False)
- Environment (dev, qa, staging, prod)
- Base URL for each environment

## Running Tests

### Run All Tests
```bash
pytest
```

### Run Specific Test File
```bash
pytest tests/test_login.py
```

### Run Tests with Different Options
```bash
# Run in headless mode
pytest --headless

# Run with custom browser
pytest --browser=firefox

# Run specific test
pytest tests/test_login.py::TestLogin::test_valid_login

# Run tests with markers
pytest -m smoke
```

### Run Tests in Different Environments

Modify `config/config.py` to change the `CURRENT_ENV` variable:

```python
CURRENT_ENV = 'staging'  # Change to desired environment
```

## Test Scenarios Included

### 1. User Login Tests
- **Valid Credentials**: Tests successful login with correct credentials
- **Invalid Credentials**: Tests error handling with wrong credentials

### 2. Navigation Tests
- **Explore Link**: Tests navigation from insights to explore page

### 3. Search Functionality Tests
- **Valid Search**: Tests search with results
- **No Results Search**: Tests search with no matching results

### 4. Asset Classes Verification
- **Profile Settings**: Verifies correct asset classes are selected

## Viewing Reports

### HTML Report
After running tests, view the HTML report:
```
reporting/report.html
```
Open this file in your web browser to see detailed test results.

### Logs
Test execution logs are saved in the `logs/` folder with timestamps:
```
logs/test_run_YYYYMMDD_HHMMSS.log
```

### Screenshots
Failed tests automatically capture screenshots saved in the `screenshots/` folder.

## Project Structure

```
test-automation-framework/
├── tests/              # Test files
├── pages/              # Page Object classes
├── utils/              # Helper utilities
├── config/             # Configuration files
├── reporting/          # HTML reports
├── logging/            # Log configuration
├── data/               # Test data files
├── screenshots/        # Failed test screenshots
├── logs/               # Test execution logs
├── requirements.txt    # Python dependencies
├── .env               # Environment variables
├── .gitignore         # Git ignore file
├── pytest.ini         # Pytest configuration
└── README.md          # This file
```

## Customization

### Adding New Tests
1. Create new test file in `tests/` folder
2. Follow the existing pattern using Page Object Model
3. Import required page classes
4. Use fixtures for browser setup

### Adding New Pages
1. Create new page class in `pages/` folder
2. Inherit from `BasePage` class
3. Define locators and methods
4. Include logging for actions

### Changing Browser Settings
Edit `config/config.py`:
```python
BROWSER = 'chromium'    # chromium, firefox, webkit
HEADLESS = False        # True for headless mode
```

### Environment Configuration
Add new environments in `config/config.py`:
```python
ENVIRONMENTS = {
    'dev': 'https://dev.platform.abc.com',
    'qa': 'https://qa.platform.abc.com',
    'staging': 'https://staging.platform.abc.com',
    'prod': 'https://platform.abc.com',
    'local': 'http://localhost:3000'  # Add new environment
}
```

## Troubleshooting

### Common Issues

**1. Playwright not installed**
```bash
playwright install
```

**2. Environment variables not loading**
- Ensure `.env` file exists in project root
- Check file format and spelling

**3. Tests failing due to timeouts**
- Increase timeout in `config/config.py`
- Check if elements exist on the page

**4. Browser not launching**
- Try different browser: `--browser=firefox`
- Check if running in headless mode

### Getting Help

1. Check test logs in `logs/` folder
2. Review screenshots for failed tests
3. Verify element selectors are correct
4. Ensure test environment is accessible

## Best Practices

1. **Keep tests simple and focused**
2. **Use meaningful test and method names**
3. **Add proper assertions**
4. **Handle waits properly**
5. **Keep page objects clean**
6. **Use logging for debugging**
7. **Regular maintenance of selectors**

## Contributing

1. Follow existing code structure
2. Add logging for new actions
3. Update README for new features
4. Test changes before committing
5. Use descriptive commit messages