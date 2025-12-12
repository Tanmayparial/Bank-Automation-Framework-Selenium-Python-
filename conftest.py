import pytest
import allure
from utils.driver_factory import get_driver
from selenium.common.exceptions import WebDriverException

# hook to attach report results on item
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

@pytest.fixture(scope="function")
def driver(request):
    driver = get_driver(headless=False)  # set headless=True if you prefer

    yield driver

    # after test: if failed, attach screenshot to allure
    try:
        if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
            try:
                screenshot = driver.get_screenshot_as_png()
                allure.attach(screenshot, name="screenshot", attachment_type=allure.attachment_type.PNG)
            except WebDriverException:
                # couldn't take screenshot
                pass
    except Exception:
        pass
    finally:
        driver.quit()
