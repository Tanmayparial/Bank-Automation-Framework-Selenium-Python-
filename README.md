# 🏦 Bank Automation Framework (Selenium + Python)

[![Python](https://img.shields.io/badge/Python-3.10+-blue)](https://www.python.org/)  
[![Selenium](https://img.shields.io/badge/Selenium-WebDriver-orange)](https://www.selenium.dev/)  
[![PyTest](https://img.shields.io/badge/PyTest-Testing-green)](https://docs.pytest.org/)  
[![Allure](https://img.shields.io/badge/Allure-Reporting-red)](https://docs.qameta.io/allure/)  
[![Build Status](https://img.shields.io/github/actions/workflow/status/<username>/<repo>/python-ci.yml?branch=main)](https://github.com/<username>/<repo>/actions)  
[![Tests Passing](https://img.shields.io/badge/Tests-Passing-brightgreen)](https://github.com/<username>/<repo>/actions)  

---

## **Project Overview**
This project is a **professional automation framework** built using **Selenium WebDriver** and **Python**, designed to automate testing of core banking functionalities on the [ParaBank demo website](https://parabank.parasoft.com/).  

The framework demonstrates **real-world test automation practices**, including:
- Page Object Model (POM) structure for maintainable and reusable code
- Data-driven testing using Excel/CSV files
- Dynamic waits and smart locators for stable test execution
- Screenshots on failure for debugging
- HTML reports using **Allure**
- CI/CD integration with **GitHub Actions**
- Parallel test execution using `pytest-xdist`
- Logging and detailed test reporting

This project is ideal for **interviews, portfolio showcases, and practical learning** in automation testing.

---

## **Table of Contents**
- [Features](#features)  
- [Tech Stack](#tech-stack)  
- [Project Structure](#project-structure)  
- [Setup & Installation](#setup--installation)  
- [Running Tests](#running-tests)  
- [Test Data Management](#test-data-management)  
- [Usage Instructions](#usage-instructions)  
- [CI/CD Integration](#cicd-integration)  
- [Contributing](#contributing)  
- [Why This Project is Valuable](#why-this-project-is-valuable)  

---

## **Features**
### Core Automation Scenarios
1. **Login Automation**  
   - Valid and invalid login workflows  
   - Error message validation  
   - Screenshot capture on test failure  
   - Allure logging of steps  

2. **Open New Account**  
   - Choose account type (Savings or Checking)  
   - Select funding account  
   - Validate success message  
   - Verify new account appears in "Accounts Overview"  

3. **Fund Transfer**  
   - Select source and destination accounts  
   - Enter transfer amount  
   - Validate success message  
   - Confirm updated balances in both accounts  
   - Full logging and Allure steps  

4. **Transaction History Validation**  
   - Validate table data: date format, description, amount  
   - Download CSV and compare with UI  
   - Ensure consistency between UI and exported data  

5. **Bill Payment Automation**  
   - Add payee information  
   - Enter account and payment amount  
   - Submit and verify confirmation messages  

6. **Profile Update**  
   - Update personal information: address, phone, email  
   - Validate success messages  
   - Positive and negative scenario testing  

7. **Logout Automation**  
   - Verify proper session closure  
   - Validate logout functionality  

### Advanced Features
- Dynamic waits and smart locators for stable tests  
- Data-driven testing via Excel/CSV for multiple scenarios  
- Automatic screenshots for failed tests  
- Allure HTML reports with detailed step logs  
- Parallel test execution using `pytest-xdist`  
- CI/CD integration with GitHub Actions for automated testing  
- Test retries for flaky tests  
- WebDriver Manager for automated ChromeDriver management  

---

## **Tech Stack**
- **Python 3.10+**  
- **Selenium WebDriver**  
- **PyTest**  
- **Page Object Model (POM)**  
- **Allure Reporting**  
- **Excel/CSV** (data-driven testing)  
- **GitHub Actions** (CI/CD Pipeline)  
- **WebDriver Manager**  

---

## **Project Structure**
bank_automation/
-  │── .github/workflows/python-ci.yml # CI/CD workflow
-  │── data/ # Test data files
-  │ ├── credentials.xlsx
-  │ └── transfer_data.xlsx
-  │── pages/ # POM classes
-  │ ├── login_page.py
-  │ ├── home_page.py
-  │ ├── transfer_page.py
-  │ ├── account_page.py
-  │ └── profile_page.py
-  │── tests/ # PyTest test cases
-  │ ├── test_login.py
-  │ ├── test_open_account.py
-  │ ├── test_transfer_funds.py
-  │ ├── test_transactions.py
-  │ └── test_profile_update.py
-  │── utils/ # Helper utilities
-  │ ├── driver_factory.py
-  │ ├── data_reader.py
-  │ ├── data_export.py
-  │ └── logger.py
-  │── conftest.py # PyTest fixtures
-  │── requirements.txt # Python dependencies
-  │── pytest.ini # PyTest configuration
-  │── README.md # Project documentation
