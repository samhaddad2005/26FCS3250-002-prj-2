# ============================================================
# CS3250 - Project 2: CampusEats
# US3 - Browse Available Food Listings
# Automated Black-Box Testing with Selenium
#
# Author: Hai-Dang Nguyen Le
# Team: TBD
#
# Generative AI Usage:
# ChatGPT was used to help design test cases, explain Selenium
# concepts, suggest code structure, and review implementation.
# The student is responsible for understanding, reviewing,
# testing, and verifying the submitted code.
# ============================================================

# IMPORTS
import pytest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

# ============================================================
# SHARED FUNCTION: Log in as a student.
# ============================================================
def login_student(driver):

    # Step 1: Open the login page.
    driver.get("http://localhost:5000/login")

    # Step 2: Find the email and password fields.
    email_input = driver.find_element(By.ID, "email")
    password_input = driver.find_element(By.ID, "password")

    # Step 3: Enter student credentials.
    email_input.send_keys(os.environ["TEST_STUDENT_EMAIL"])
    password_input.send_keys(os.environ["TEST_STUDENT_PASSWORD"])

    # Step 4: Find and click the Login button.
    login_button = driver.find_element(By.ID, "submit")
    login_button.click()

    # Step 5: Wait for successful login.
    WebDriverWait(driver, 10).until(
        EC.url_to_be("http://localhost:5000/")
    )


# ============================================================
# TC01: Verify available listings are displayed.
# ------------------------------------------------------------
# Preconditions:
# - CampusEats is running.
# - A valid student account exists.
# - A Pizza listing exists in the database.
# - Pizza has 5 remaining portions.
# - Pizza is not cancelled.
# - Pizza's pickup window has not ended.
#
# Test Steps:
# 1. Launch Chrome.
# 2. Log in as a student.
# 3. Open the food listings page.
# 4. Locate the Pizza listing.
# 5. Verify that Pizza is displayed.
#
# Expected Result:
# - Pizza is visible on the food listings page.
#
# Postconditions:
# - The browser session is closed.
# - No listing data is modified.
# ============================================================
def test_available_listing():
    # Step 1: Launch the Chrome browser.
    driver = webdriver.Chrome()
    try:
        # Step 2: Log in as a student.
        login_student(driver)

        # 3.1 Open the food listings page.
        driver.get("http://localhost:5000/listings")
        # 3.2 Verify that the listings page loaded successfully.
        assert "404 not found" not in driver.title.lower()

        # Step 4: Locate the Pizza listing title.
        pizza_listing = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//*[contains(@class, 'listing-title') and normalize-space(.)='Pizza']")
            )
        )

        # Step 5: Verify that Pizza is displayed.
        assert pizza_listing.is_displayed()

    finally:
        # Step 6: Close the browser.
        driver.quit()
    

# ============================================================
# TC02: Verify listings with zero portions are hidden.
#
# Preconditions:
# - CampusEats is running.
# - A valid student account exists.
# - A Burger listing exists in the database.
# - Burger has 0 remaining portions.
#
# Test Steps:
# 1. Launch Chrome.
# 2. Log in as a student.
# 3. Open the food listings page.
# 4. Search for the Burger listing.
# 5. Verify that Burger is not displayed.
#
# Expected Result:
# - Burger is not visible on the food listings page.
#
# Postconditions:
# - The browser session is closed.
# - No listing data is modified.
# ============================================================
def test_zero_portions_hidden():
    # 1. Launch Chrome.
    driver = webdriver.Chrome()
    try:
        # 2. Log in as a student.
        login_student(driver)
        # 3.1 Open the food listings page.
        driver.get("http://localhost:5000/listings")
        # 3.2 Verify that the listings page loaded successfully.
        assert "404 not found" not in driver.title.lower()
        # 4. Search for the Burger listing.
        burger_listings = driver.find_elements(
            By.XPATH,
            "//*[contains(concat(' ', normalize-space(@class), ' '), ' listing-title ') and normalize-space(.)='Burger']"
        )
        # 5. Verify that Burger is not displayed.
        assert len(burger_listings)==0
    finally:
        # Step 6: Close the browser.
        driver.quit()

# ============================================================
# TC03: Verify expired listings are hidden.
#
# Preconditions:
# - CampusEats is running.
# - A valid student account exists.
# - A Sandwich listing exists in the database.
# - Sandwich has 5 remaining portions.
# - Sandwich is not cancelled.
# - Sandwich's pickup_end time is in the past.
#
# Test Steps:
# 1. Launch Chrome.
# 2. Log in as a student.
# 3. Open the food listings page.
# 4. Search for the Sandwich listing.
# 5. Verify that Sandwich is not displayed.
#
# Expected Result:
# - Sandwich is not visible on the food listings page.
#
# Postconditions:
# - The browser session is closed.
# - No listing data is modified.
# ============================================================
def test_expired_listing_hidden():
    # 1. Launch Chrome.
    driver = webdriver.Chrome()
    try:
        # 2. Log in as a student.
        login_student(driver)
        # 3.1 Open the food listings page.
        driver.get("http://localhost:5000/listings")
        # 3.2 Verify that the listings page loaded successfully.
        assert "404 not found" not in driver.title.lower()
        # 4. Search for the Sandwich listing.
        sandwich_listings = driver.find_elements(
            By.XPATH,
            "//*[contains(concat(' ', normalize-space(@class), ' '), ' listing-title ') and normalize-space(.)='Sandwich']"
         )
        # 5. Verify that Sandwich is not displayed.
        assert len(sandwich_listings) == 0
    finally: 
        # Step 6: Close the browser.
        driver.quit()
         


# ============================================================
# TC04: Verify cancelled listings are hidden.
#
# Preconditions:
# - CampusEats is running.
# - A valid student account exists.
# - A Salad listing exists in the database.
# - Salad has 5 remaining portions.
# - Salad's pickup window has not ended.
# - Salad's status is cancelled.
#
# Test Steps:
# 1. Launch Chrome.
# 2. Log in as a student.
# 3. Open the food listings page.
# 4. Search for the Salad listing.
# 5. Verify that Salad is not displayed.
#
# Expected Result:
# - Salad is not visible on the food listings page.
#
# Postconditions:
# - The browser session is closed.
# - No listing data is modified.
# ============================================================
def test_cancelled_listing_hidden():
    # 1. Launch Chrome.
    driver = webdriver.Chrome()
    try:
        # 2. Log in as a student.
        login_student(driver)
        # 3.1 Open the food listings page.
        driver.get("http://localhost:5000/listings")
        # 3.2 Verify that the listings page loaded successfully.
        assert "404 not found" not in driver.title.lower()
        # 4. Search for the Salad listing.
        salad_listings = driver.find_elements(
            By.XPATH,
            "//*[contains(concat(' ', normalize-space(@class), ' '), ' listing-title ') and normalize-space(.)='Salad']"
        )
        # 5. Verify that Salad is not displayed.
        assert len(salad_listings) == 0
    finally: 
        # Step 6: Close the browser.
        driver.quit()


# ============================================================
# TC05: Verify all required listing details are displayed.
#
# Preconditions:
# - CampusEats is running.
# - A valid student account exists.
# - A Pizza listing exists in the database.
# - Pizza has 5 remaining portions.
# - Pizza is available and not expired.
# - Pizza has known pickup start and end times.
#
# Test Steps:
# 1. Launch Chrome.
# 2. Log in as a student.
# 3. Open the food listings page.
# 4. Locate the Pizza listing.
# 5. Verify that all required listing details are displayed.
#
# Expected Result:
# - The Pizza listing displays its title.
# - The remaining portions are displayed.
# - The pickup start time is displayed.
# - The pickup end time is displayed.
#
# Postconditions:
# - The browser session is closed.
# - No listing data is modified.
# ============================================================
def test_listing_details():
    # Step 1: Launch the Chrome browser.
    driver = webdriver.Chrome()
    try:
        # Step 2: Log in as a student.
        login_student(driver)

        # 3.1 Open the food listings page.
        driver.get("http://localhost:5000/listings")
        # 3.2 Verify that the listings page loaded successfully.
        assert "404 not found" not in driver.title.lower()

        # Step 4: Find the Pizza listing.
        pizza_listing = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//*[contains(@class, 'listing-title') and normalize-space(.)='Pizza']")
            )
        )
        # Step 5.1: Locate the parent listing container for Pizza.
        pizza_container = pizza_listing.find_element(
            By.XPATH, "./ancestor::*[contains(concat(' ', normalize-space(@class), ' '), ' listing ')][1]"
        )
        # Step 5.2: Locate and verify Pizza's remaining portions.
        portions_element = pizza_container.find_element(
            By.CSS_SELECTOR, ".listing-portions"
        )
        assert portions_element.text.strip() == "5"
        # Step 5.3: Locate and verify Pizza's pickup start time.
        pickup_start_element = pizza_container.find_element(
            By.CSS_SELECTOR, ".listing-pickup-start"
        )
        assert pickup_start_element.text.endswith("11:00 AM")
        # Step 5.4: Locate and verify Pizza's pickup end time.
        pickup_end_element = pizza_container.find_element(
            By.CSS_SELECTOR, ".listing-pickup-end"
        )
        assert pickup_end_element.text.endswith("1:00 PM")
    finally:
        # Step 6: Close the browser.
        driver.quit()


# ============================================================
# TC06: Verify listings are sorted by pickup end time.
#
# Preconditions:
# - CampusEats is running.
# - A valid student account exists.
# - Three available listings exist with different pickup end times.
#
# Test Steps:
# 1. Launch Chrome.
# 2. Log in as a student.
# 3. Open the food listings page.
# 4. Retrieve the pickup end times in display order.
# 5. Verify the times are sorted in ascending order.
#
# Expected Result:
# - Listings appear from earliest to latest pickup end time.
#
# Postconditions:
# - The browser session is closed.
# - No listing data is modified.
# ============================================================
def test_listing_sort_order():
    # Step 1: Launch the Chrome browser.
    driver = webdriver.Chrome()
    try:
        # Step 2: Log in as a student.
        login_student(driver)

        # 3.1 Open the food listings page.
        driver.get("http://localhost:5000/listings")
        # 3.2 Verify that the listings page loaded successfully.
        assert "404 not found" not in driver.title.lower()

        # Step 4: Retrieve all pickup end times in display order.
        # Step 4.1: Locate all listing containers in display order.
        listing_elements = driver.find_elements(
            By.CSS_SELECTOR, "#listings .listing"
        )
        # Step 4.2: Extract pickup end times from listing attributes.
        pickup_end_times = [
            element.get_attribute("data-pickup-end")
            for element in listing_elements
        ]
        
        # Step 5: Verify pickup end times are sorted in ascending order.
        # Step 5.1: Verify that at least two listings exist.
        assert len(pickup_end_times) >= 2
        # Step 5.2: Verify pickup end times are sorted in ascending order.
        assert all(pickup_end_times)
        assert pickup_end_times == sorted(pickup_end_times)

    finally:
        # Step 6: Close the browser.
        driver.quit()
    
# ============================================================
# TC07: Verify the empty-state message is displayed.
#
# Preconditions:
# - CampusEats is running.
# - A valid student account exists.
# - No available food listings exist in the database.
#
# Test Steps:
# 1. Launch Chrome.
# 2. Log in as a student.
# 3. Open the food listings page.
# 4. Locate the empty listings message.
# 5. Verify that the message is displayed correctly.
#
# Expected Result:
# - An informative message is displayed when no listings
#   are available.
#
# Postconditions:
# - The browser session is closed.
# - No listing data is modified.
# ============================================================
def test_empty_listings_message():
    # Step 1: Launch Chrome.
    driver = webdriver.Chrome()

    try:
        # Step 2: Log in as a student.
        login_student(driver)

        # Step 3: Open the food listings page.
        # and Verify that the page is not a 404 error.
        driver.get("http://localhost:5000/listings")
        assert "404 not found" not in driver.title.lower()
        # Step 4: Locate the empty listings message.
        empty_message = driver.find_element(By.ID, "no-listings")
        # 5. Verify that the message is displayed correctly.
        # Step 5.1: Verify the empty listings message is displayed.
        assert empty_message.is_displayed()
        # Step 5.2: Verify that the listings container does not exist.
        assert len(driver.find_elements(By.ID, "listings")) == 0

    finally:
        driver.quit()