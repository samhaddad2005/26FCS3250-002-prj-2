"""US7 black-box tests against a running CampusEats app (see README)."""

import os
import re
from datetime import datetime, timedelta
from uuid import uuid4

import pytest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

BASE_URL = os.getenv("TEST_BASE_URL", "http://localhost:5000").rstrip("/")
PASSWORD = "US7TestPassword123!"


def wait_for(browser, condition, description, timeout=10):
    try:
        return WebDriverWait(browser, timeout).until(condition)
    except TimeoutException:
        pytest.fail(
            f"Timed out waiting for {description} at {browser.current_url}.\n"
            f"Page showed:\n{browser.find_element(By.TAG_NAME, 'body').text}",
            pytrace=False,
        )


@pytest.fixture(scope="module")
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1280,900")
    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(20)
    try:
        driver.get(f"{BASE_URL}/register")
        wait_for(
            driver,
            EC.visibility_of_element_located((By.ID, "email")),
            f"CampusEats at {BASE_URL}; start the app or set TEST_BASE_URL",
        )
        yield driver
    finally:
        driver.quit()


@pytest.fixture(scope="module")
def accounts(browser):
    """Register new accounts each run instead of consuming a seeded code."""
    unique = uuid4().hex[:12]
    accounts = {}
    for key, role in (
        ("owner", "vendor"),
        ("other_vendor", "vendor"),
        ("student", "student"),
        ("other_student", "student"),
    ):
        account = {
            "name": f"US7 {key} {unique}",
            "email": f"us7_{key}_{unique}@example.com",
        }
        browser.get(f"{BASE_URL}/register")
        for field in ("name", "email"):
            browser.find_element(By.ID, field).send_keys(account[field])
        browser.find_element(By.ID, "password").send_keys(PASSWORD)
        browser.find_element(By.ID, "password_confirm").send_keys(PASSWORD)
        Select(browser.find_element(By.ID, "role")).select_by_value(role)
        browser.find_element(By.ID, "submit").click()
        wait_for(browser, EC.url_to_be(f"{BASE_URL}/login"), "registration")
        accounts[key] = account
    return accounts


def login(browser, account):
    browser.delete_all_cookies()
    browser.get(f"{BASE_URL}/login")
    browser.find_element(By.ID, "email").send_keys(account["email"])
    browser.find_element(By.ID, "password").send_keys(PASSWORD)
    browser.find_element(By.ID, "submit").click()
    wait_for(browser, EC.url_to_be(f"{BASE_URL}/"), "login")


def create_listing(browser, pickup_end=None):
    title = f"US7 pickup {uuid4().hex[:12]}"
    now = datetime.now()
    browser.get(f"{BASE_URL}/create_listing")
    for field, value in {
        "title": title,
        "description": "Food for the US7 Selenium test",
        "portions": "4",
        "pickup_location": "US7 Test Counter",
    }.items():
        element = browser.find_element(By.ID, field)
        element.clear()
        element.send_keys(value)

    # Set native datetime-local controls without locale-dependent key presses.
    for field, value in {
        "pickup_start": now - timedelta(minutes=5),
        "pickup_end": pickup_end or now + timedelta(hours=1),
    }.items():
        browser.execute_script(
            "arguments[0].value = arguments[1];"
            "arguments[0].dispatchEvent(new Event('input', {bubbles: true}));"
            "arguments[0].dispatchEvent(new Event('change', {bubbles: true}));",
            browser.find_element(By.ID, field),
            value.strftime("%Y-%m-%dT%H:%M"),
        )
    browser.find_element(By.ID, "submit").click()
    wait_for(browser, EC.url_to_be(f"{BASE_URL}/"), "listing creation")
    return title


def reserve_listing(browser, title, portions=1):
    browser.get(f"{BASE_URL}/listings")
    listing = wait_for(
        browser,
        EC.visibility_of_element_located(
            (By.XPATH, f"//li[@data-listing-id][.//h2[text()='{title}']]")
        ),
        f"listing {title}",
    )
    Select(listing.find_element(By.NAME, "portions")).select_by_value(str(portions))
    listing.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    wait_for(browser, EC.staleness_of(listing), "reservation navigation")
    body = wait_for(
        browser,
        EC.presence_of_element_located((By.TAG_NAME, "body")),
        "reservation response",
    ).text
    match = re.fullmatch(r"Reservation successful! Pickup code: (\d{6})", body)
    assert match, f"Reservation failed at {browser.current_url}: {body}"
    return match.group(1)


def submit_pickup_code(browser, code):
    browser.get(f"{BASE_URL}/confirm_pickup")
    field = browser.find_element(By.ID, "pickup_code")
    field.clear()
    field.send_keys(code)
    browser.find_element(By.ID, "submit").click()
    wait_for(browser, EC.staleness_of(field), "pickup submission")
    return wait_for(
        browser,
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".flash")),
        "pickup result",
    ).text


def test_only_listing_owner_can_confirm_pickup_once(browser, accounts):
    login(browser, accounts["owner"])
    title = create_listing(browser)
    login(browser, accounts["student"])
    code = reserve_listing(browser, title, portions=2)

    login(browser, accounts["other_vendor"])
    assert submit_pickup_code(browser, code) == (
        "No reservation with that pickup code was found for your listings."
    )

    login(browser, accounts["owner"])
    # Generated pickup codes are numeric, so this six-character code cannot exist.
    assert submit_pickup_code(browser, "BAD123") == (
        "No reservation with that pickup code was found for your listings."
    )
    assert submit_pickup_code(browser, code) == (
        f"Pickup confirmed for {accounts['student']['name']}. Portions to hand out: 2"
    )
    assert submit_pickup_code(browser, code) == "This reservation is no longer active."


def test_expired_pickups_are_rejected_and_shown_as_no_shows(browser, accounts):
    login(browser, accounts["owner"])
    # Forms accept minute precision. Leave at least 30 seconds to reserve twice.
    pickup_end = (datetime.now() + timedelta(seconds=90)).replace(
        second=0, microsecond=0
    )
    title = create_listing(browser, pickup_end=pickup_end)
    codes = []
    for student in (accounts["student"], accounts["other_student"]):
        login(browser, student)
        codes.append(reserve_listing(browser, title))

    login(browser, accounts["other_vendor"])
    browser.get(f"{BASE_URL}/confirm_pickup")
    assert title not in browser.find_element(By.TAG_NAME, "main").text

    login(browser, accounts["owner"])
    browser.get(f"{BASE_URL}/confirm_pickup")
    assert title not in browser.find_element(By.TAG_NAME, "main").text

    # Observe real expiry through the UI; do not change application data or time.
    def both_no_shows_visible(driver):
        driver.refresh()
        rows = [row.text for row in driver.find_elements(By.CSS_SELECTOR, "main li")]
        return all(
            f"{title} - {student['name']} (1 portion(s)) - No-show" in rows
            for student in (accounts["student"], accounts["other_student"])
        )

    wait_for(browser, both_no_shows_visible, "both no-show rows", timeout=95)
    for code in codes:
        assert submit_pickup_code(browser, code) == "The pickup window has ended."

    login(browser, accounts["other_vendor"])
    browser.get(f"{BASE_URL}/confirm_pickup")
    assert title not in browser.find_element(By.TAG_NAME, "main").text
